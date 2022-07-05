#!/usr/bin/env python

from preprocessing import preprocessing as preprocess
from hive import hive as hive
from miscellaneous import miscell as report
from visualization import visualization as vui

####### Pre-Processing of data ##########
path_input = '../data/input/Dataset_movie.txt'
data_array = preprocess.read_file(path_input)
csv_data = preprocess.data_to_csv(data_array)
valida_data=[]
for d in csv_data:
    valida_data.append(preprocess.handle_null_time(d))
preprocess.fetch_and_convert_data(valida_data)

path_output = '../data/output/updated_dataset'
preprocess.write_file(path_output,valida_data)

###### Hive and HQL queries ########
conn = hive.connection_setup('localhost',10000,'hive')
cursor = hive.create_cursor(conn)
cursor.execute('create database if not exists project')
cursor.execute('use project')
hive.drop_table(cursor,"project","temp_movie")
hive.drop_table(cursor,"project","movie")

cursor.execute("create table if not exists temp_movie (id  int,title string, year int,rating float, dur int) row format delimited fields terminated by ','")
cursor.execute("load data inpath '/tmp/updated_dataset' into table temp_movie ")
cursor.execute("set hive.exec.dynamic.partition = true")
cursor.execute("set hive.exec.dynamic.partition.mode = nonstrict")
cursor.execute("create table if not exists movie (id  int,title string, year int, dur int) partitioned by (rating float) row format delimited fields terminated by ','")
cursor.execute("insert into table movie PARTITION (rating) select id,title,year,dur,rating from temp_movie")

writeDir = {}
print("Total number of movies:")
cursor.execute("select count(*) from movie")
num_of_movie = cursor.fetchone()[0]
print(num_of_movie)
writeDir["Total number of movies: "]= num_of_movie

print("Maximum rating given to any movie:")
cursor.execute("select max(rating) from movie")
max_rating = cursor.fetchall()[0]
print(max_rating)
writeDir["Maximum rating given to any movie:"] = max_rating

print("Movie with max rating:")
cursor.execute('select title,rating from movie where rating=(select max(rating) from movie)')
mov_max_rating = cursor.fetchall()
print(mov_max_rating)
writeDir["Movie with max rating:"] = mov_max_rating

print("Years and number of movies release each year:")
cursor.execute("select year,count(year) from movie group by year ")
movPerYear = cursor.fetchall()
print(movPerYear)
writeDir["Year and number of movies release each year:"] = movPerYear

print("Movie Distribution as per ratings")
cursor.execute("select rating,count(rating) from movie group by rating")
movPerRating = cursor.fetchall()
print(movPerRating)
writeDir["Movie Distribution as per ratings"] = movPerRating
 
####### Write and Read report 
report.write_report(writeDir)
queryReport = report.read_report()

####stemplot for movie/year
xplot,yplot=vui.createaxis('Year and number of movies release each year:',queryReport)
vui.createStemPlot(xplot,yplot,'Year','Number of movies','Number of movies/year','../data/output/movieperyear.png')
#### stemplot for movie/ratings
xplot,yplot=vui.createaxis('Movie Distribution as per ratings',queryReport)
vui.createStemPlot(xplot,yplot,'Year','Number of movies','Number of movies/rating','../data/output/movieperrating.png')

######## Example for UDF ######
cursor.execute('add file hdfs:///tmp/time_convert.py')

print("Convert duration from sec to hh:mm:ss")
cursor.execute("select transform (id,title,year,rating,dur) using 'python3 time_convert.py' as (transformed) from (select id,title,year,rating,dur from movie where rating=4.0 limit 1) movie")
print(cursor.fetchone())

####### Drop table ######
# hive.drop_table(cursor,"project","temp_movie")
# hive.drop_table(cursor,"project","movie")


# BIGDATA-Project-MovieDataReview
![logo](https://github.com/shubham7151/BIGDATA-Project-MovieDataReview/blob/master/src/image/logo.png "imdb logo")

# Problem Statement
- The Internet Movie Database (IMDb) is one of the world’s most popular sources for movie, TV and celebrity content with more than 100 million unique visitors per month.
- IMDb has huge collection of movies database that includes various details of movies along with different ratings and user reviews.
- This movie reviews affects everyone from audience, film critics to the production company.
- The idea of project is to analyse the movie and ratings dataset (source: https://www.simplilearn.com/) using big data technologies. 

# DataSet
- 49000+ records with 5 colums {id, title, year, rating, duration}
  - id: The Identification number of the records, act as primary key
  - title: The name of the movie, TV show or celebrity content
  - year: The year the content was released
  - rating: the rating given to the content, ranges from (1-5)
  - duration: the time span of the content (in seconds)
- Data is stored as csv. 

# Solution
- Store test dataset in a hive table for initial analysis. 
- Pre-process the data to handle null value.
- Transfer the precessed data to a partitioned hive table.
- Setup a Hive Thrift Server to interact with hive table using python. 
- Use Hive queries to extract data and for analysis. 
- The insights Could be found under doc/report.

# Big Data Technologies & Mind Map
![mindmap](https://github.com/shubham7151/BIGDATA-Project-MovieDataReview/blob/master/src/image/mindmap.png "mind map")

# Project directory tree
![project tree](https://github.com/shubham7151/BIGDATA-Project-MovieDataReview/blob/master/src/image/Screenshot%20from%202022-07-05%2016-03-48.png "project tree")

# Challenges
- Handling the null values for different columns like duration, rating, year. 
- Hive support timestamp datatype but duration was given in seconds hence it required UDF to convert it to time format (HH:MM:SS)
   





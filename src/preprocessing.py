# import time 

# raw_data = open('../data/input/Dataset_movie.txt')
# data_array= raw_data.readlines()
# csv_data_format = []
# for data in data_array:
#     if not data.isspace():
#         csv_data_format.append( data.split(',') )

# print("data csv format")
# print(csv_data_format[-1])


# print("time")


# print(time.strftime('%H:%M:%S',time.gmtime(float(csv_data_format[1][-1]))))

# # csv_data =[]
# # for data in data_array:
# #     data

# # 
#!/usr/bin/env python

from itertools import count
import time
def read_file(path):
    with open(path,'r') as raw_data :
        data_array= raw_data.readlines()
    return data_array

def data_to_csv (data_array) :
    csv_data_format = []
    for data in data_array:
        if not data.isspace():
            csv_data_format.append( data.split(',') )
        valid_data = map(lambda x : int(x),)
    return csv_data_format

def sec_to_hours (seconds):
    return time.strftime('%H:%M:%S',time.gmtime(float(seconds[-1])))

def handle_null_time(time_index):
    if time_index[-1]==']\n':
        time_index[-1] = -1
    return time_index

def fetch_and_convert_data (csv_dataindex):
    count=0
    for index in csv_dataindex:
        print(sec_to_hours(index))
        count= count +1
        print(index)
        print(count)
    # print("count")
    # print(count)

    

path = '../data/input/temp_data.txt'
data_array = read_file(path)
csv_data = data_to_csv(data_array)
for d in csv_data:
    valida_data = handle_null_time(d)
    print(valida_data)
# print(csv_data[13])
# fetch_and_convert_data(csv_data)


# print(csv_data)
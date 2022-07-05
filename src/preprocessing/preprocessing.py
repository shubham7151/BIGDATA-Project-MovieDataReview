#!/usr/bin/env python

def read_file(path):
    with open(path,'r') as raw_data :
        data_array= raw_data.readlines()
    return data_array

def write_file(path,dataToWrite):
    import csv
    try:
        with open (path,'w') as file:
            w = csv.writer(file,delimiter=',')
            w.writerows(dataToWrite)
    except:
        print("Writing unsucessfull")

def data_to_csv (data_array) :
    csv_data_format = []
    for data in data_array:
        if not data.isspace():
            csv_data_format.append( data.split(',') )
    return csv_data_format

def sec_to_hours (seconds):
    import time
    return time.strftime('%H:%M:%S',time.gmtime(float(seconds[-1])))

def handle_null_time(time_index):
    if time_index[-1]=='\n':
        time_index[-1] = -1
    return time_index

def fetch_and_convert_data (csv_dataindex):
    for index in csv_dataindex:
        if index[-1] == -1:
            pass
        else:
            index[-1]=int(index[-1])

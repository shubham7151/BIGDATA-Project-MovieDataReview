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


def read_file(path):
    with open(path,'r') as raw_data :
        data_array= raw_data.readlines()
    return data_array

def write_file(path,dataToWrite):
    import csv
    try:
        with open ("../data/output/output",'w') as file:
            w = csv.writer(file,delimiter=',')
            w.writerows(valida_data)
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
            index[-1]=sec_to_hours(index)

path_input = '../data/input/Dataset_movie.txt'
data_array = read_file(path_input)
csv_data = data_to_csv(data_array)
valida_data=[]
for d in csv_data:
    valida_data.append(handle_null_time(d))
fetch_and_convert_data(valida_data)

path_output = '../data/output/updated_dataset'
write_file(path_output,valida_data)

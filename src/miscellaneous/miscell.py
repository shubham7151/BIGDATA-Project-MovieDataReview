import json

def write_report(data,path='../data/output/report'):
        try:
            with open (path,'w') as file:
                json.dump(data,file)
        except Exception as e:
            print(e)
            print("Writing unsucessfull")

def read_report():
        try:
            with open('../data/output/report','r') as report:
                return json.load(report)
        except Exception as e:
            print(e)
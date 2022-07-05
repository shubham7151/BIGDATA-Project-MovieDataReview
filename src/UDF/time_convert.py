import sys
import time
try:
    lines = sys.stdin.readlines()
    x = []
    for line in lines:
        line = line.strip('\n\r')
        temp = line.split('\t')
        print(str(temp[0])+" "+str(temp[1])+" "+str(temp[2])+" "+str(temp[3])+" "+str(time.strftime('%H:%M:%S',time.gmtime(float(temp[4])))))
except Exception as e:
    print(e)
import sys
  
try:
    lines = sys.stdin.readlines()
    x = []
    for line in lines:
        line = line.strip('\n\r')
        temp = line.split(':')
        x.append(int(int(temp[0])*3600 + int(temp[1]) * 60 + int(temp[2])))
    print(x)
    
        
except:
    print(sys.stderr.errors)
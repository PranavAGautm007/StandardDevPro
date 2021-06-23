import math 
import csv 
with open('data1.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
    print(file_data)
    
data=file_data[0]
print(data)
def mean(data):
    n = len(data)
    
    total=0
    for x in data:
        total+=int(x)
    mean = total/n
    return mean 
    print("mean:"+str(mean))

squared_list=[]
for a in data:
    b = int(a) - mean(data)
    b = b**2
    squared_list.append(b)
print(squared_list)
sum = 0
for c in squared_list:
    sum = sum + c 

result = sum/(len(data)-1)
print("result:"+str(result))
standard_deviation = math.sqrt(result)
print("The Standard Deviation for this data set is :"+str(standard_deviation))

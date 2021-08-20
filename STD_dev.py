import math
import csv 
with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data[1]

#FINDING MEAN
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total += int(x)
    mean=total/n
    return mean

#SQUIRING AND GETTING THE VALUES
squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)

#GETTING SUM
sum=0
for i in squared_list:
    sum=sum+i

#DIVIDING THE SUM BY TOTAL VALUES
result=sum/(len(data)-1)

#GETTING THE DEVIATION BY TAKING SQUARE ROOT OF THE RESULT
standard_deviation=math.sqrt(result)
print(standard_deviation) 
    
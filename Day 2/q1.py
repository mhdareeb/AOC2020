import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

count=0
for i in range(1000):
    query=input()
    data=query.split(' ')
    limits=data[0].split('-')
    minimum=int(limits[0])
    maximum=int(limits[1])
    char=data[1][:1]
    pwd=data[2]
    freq=pwd.count(char)
    if(freq>=minimum and freq<=maximum):
        count+=1
print(count)
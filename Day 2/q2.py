import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

count=0
for _ in range(1000):
    query=input()
    data=query.split(' ')
    limits=data[0].split('-')
    i=int(limits[0])
    j=int(limits[1])
    char=data[1][:1]
    pwd=data[2]
    freq=pwd.count(char)
    if((pwd[i-1]==char and pwd[j-1]!=char) or (pwd[i-1]!=char and pwd[j-1]==char)):
        count+=1
print(count)
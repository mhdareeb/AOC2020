import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

count=0
i=0
j=0
while(i<323 and j<31):
    line=input()
    if(line[j]=='#'):
        count+=1
    j=(j+3)%31
    i+=1
print(count)
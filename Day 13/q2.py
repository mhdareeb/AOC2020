import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def validProd(timestamp):
    prod=1
    for i in range(n):
        bus=buses[i]
        if(bus!='x'):
            if((timestamp+i)%bus==0):
                prod*=bus
    return prod

minTime=int(input())
line=list(input().split(','))
buses=[]
maxBus=-float('inf')
firstBus=-1
maxProd=1
for val in line:
    if(val=='x'):
        buses.append(val)
    else:
        buses.append(int(val))
        if(firstBus==-1):
            firstBus=int(val)
        maxProd*=int(val)
        maxBus=max(maxBus,int(val))

n=len(buses)
t=0
while(True):
    prod=validProd(t)
    if(prod==maxProd):
        break
    t+=prod
print(t)
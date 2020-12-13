import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

minTime=int(input())
line=list(input().split(','))
buses=[int(bus) for bus in line if bus!='x']

chosenBus=-1
waitTime=float('inf')
for bus in buses:
    wait=(((minTime//bus)+1)*bus)%minTime
    if(wait<waitTime):
        chosenBus=bus
        waitTime=wait
print(waitTime*chosenBus)
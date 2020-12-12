import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

directions={0:'east',1:'north',2:'west',3:'south'}

def steer(direction,turn, degrees):
    if(turn=='L'):
        return (direction+(degrees//90))%4
    else:
        return (direction-(degrees//90))%4

def forward(distance):
    if(direction==0):
        ferry[0]+=distance
    elif(direction==1):
        ferry[1]+=distance
    elif(direction==2):
        ferry[0]-=distance
    else:
        ferry[1]-=distance

def shift(direction,distance):
    if(direction==0):
        ferry[0]+=distance
    elif(direction==1):
        ferry[1]+=distance
    elif(direction==2):
        ferry[0]-=distance
    else:
        ferry[1]-=distance

ferry=[0,0]
direction=0
with open('../input.txt','r') as f:
    for line in f:
        instruction=line.strip()
        code=instruction[0]
        value=int(instruction[1:])
        if(code=='E'):
            shift(0,value)
        elif(code=='N'):
            shift(1,value)
        elif(code=='W'):
            shift(2,value)
        elif(code=='S'):
            shift(3,value)
        elif(code=='F'):
            forward(value)
        else:
            direction=steer(direction,code,value)
    print(abs(ferry[0])+abs(ferry[1]))
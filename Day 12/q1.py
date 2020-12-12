import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

directions={'E':0,'N':1,'W':2,'S':3}

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
        if(code=='F'):
            forward(value)
        elif(code in ['L','R']):
            direction=steer(direction,code,value)
        else:
            shift(directions[code],value)        
    print(abs(ferry[0])+abs(ferry[1]))
    f.close()
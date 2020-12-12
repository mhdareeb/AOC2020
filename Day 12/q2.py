import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

directions={0:'east',1:'north',2:'west',3:'south'}

def steer(waypoint,turn, degrees):
    x=waypoint[0]-ferry[0]
    y=waypoint[1]-ferry[1]
    direction=(degrees//90)%4
    if(turn=='R'):
        direction=(4-direction)%4
    if(direction==0):
        return waypoint
    elif(direction==1):
        waypoint=[-y,x]
    elif(direction==2):
        waypoint=[-x,-y]
    else:
        waypoint=[y,-x]
    waypoint=[ferry[0]+waypoint[0],ferry[1]+waypoint[1]]
    return waypoint

def forward(times):
    x=waypoint[0]-ferry[0]
    y=waypoint[1]-ferry[1]
    ferry[0]+=(times*x)
    ferry[1]+=(times*y)
    waypoint[0]=ferry[0]+x
    waypoint[1]=ferry[1]+y

def shift(direction,distance):
    if(direction==0):
        waypoint[0]+=distance
    elif(direction==1):
        waypoint[1]+=distance
    elif(direction==2):
        waypoint[0]-=distance
    else:
        waypoint[1]-=distance

ferry=[0,0]
waypoint=[10,1]
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
            waypoint=steer(waypoint,code,value)
        # print(ferry, waypoint)
    print(abs(ferry[0])+abs(ferry[1]))
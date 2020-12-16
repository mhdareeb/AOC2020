import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def isValid(value):
    for rule in rules:
        for limits in rule:
            if value in range(limits[0],limits[1]+1):
                return True
    return False

def scanningError(nearby):
    error=0
    for value in nearby:
        if not isValid(value):
            error+=value
    return error

with open('../input.txt','r') as f:
    rules=[]
    line=f.readline()
    while line!='\n':
        line=line.strip().split(': ')[1]
        line=line.split(' or ')
        line=[list(map(int,limits.split('-'))) for limits in line]
        rules.append(line)
        line=f.readline()
    line=f.readline()
    myticket=list(map(int,f.readline().strip().split(',')))
    line=f.readline()
    line=f.readline()
    error=0
    for nearby in f:
        nearby=list(map(int,nearby.strip().split(',')))
        error+=scanningError(nearby)
    print(error)
    f.close()    
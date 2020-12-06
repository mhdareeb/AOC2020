import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def unionLength(group):
    union=set(group[0])
    for sequence in group:
        union=union.union(set(sequence))
    return len(union)

def intersectionLength(group):
    intersection=set(group[0])
    for sequence in group:
        intersection=intersection.intersection(set(sequence))
    return len(intersection)

with open('../input.txt','r') as f:
    group=[]
    unionCount=0
    intersectionCount=0
    for line in f:
        if(line!='\n'):
            group+=[line.strip()]
        else:
            unionCount+=unionLength(group)
            intersectionCount+=intersectionLength(group)            
            group=[]
    unionCount+=unionLength(group)
    intersectionCount+=intersectionLength(group)
    print(unionCount)
    print(intersectionCount)
    f.close()
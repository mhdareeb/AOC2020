import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def findLoop(lineNo):
    global accumulator
    if(visited[lineNo]):
        return
    instruction=graph[lineNo][0]
    payload=int(graph[lineNo][1])
    visited[lineNo]=1
    if(instruction=='nop'):
        findLoop(lineNo+1)
    elif(instruction=='jmp'):
        findLoop(lineNo+payload)
    else:
        accumulator+=payload
        findLoop(lineNo+1)

graph={}
visited={}
with open('../input.txt','r') as f:
    for i,line in enumerate(f):
        line=line.strip()
        line=line.split()
        graph[i]=line
        visited[i]=0
    f.close()

accumulator=0
findLoop(0)
print(accumulator)
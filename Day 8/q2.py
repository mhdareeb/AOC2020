import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def findLoop(lineNo):
    global accumulator
    global flag
    if(lineNo<len(graph)):
        if(visited[lineNo]):
            flag=1
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

def reset():
    for key in graph:
        visited[key]=0

def findCorrupt():
    global flag
    global accumulator
    for lineNo in graph:
        instruction=graph[lineNo][0]
        payload=int(graph[lineNo][1])
        if(instruction=='acc'):
            continue
        else:
            flag=0
            accumulator=0
            reset()
            if(instruction=='jmp'):
                graph[lineNo][0]='nop'
            else:
                graph[lineNo][0]='jmp'
            findLoop(0)
            graph[lineNo][0]=instruction
            if not flag:
                break

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
flag=0
findCorrupt()
print(accumulator)
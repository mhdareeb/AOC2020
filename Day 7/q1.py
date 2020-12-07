import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def DFS_visit(container):
    global count
    global flag
    if container=='shiny gold':
        flag=1
        count+=1
        return
    if visiting[container]==0:
        visiting[container]=1
        for holding in graph[container]:
            if visiting[holding]==0:
                DFS_visit(holding)
                if(flag==1):
                    return
        visiting[container]=2

def reset(graph):
    for key in graph:
        visiting[key]=0

def DFS(graph):
    global flag
    for key in graph:
        if key!='shiny gold':
            flag=0
            reset(graph)
            DFS_visit(key)

def extractHoldings(contents):
    holdings=[]
    contents=contents.split(' ')
    i=0
    while(i<len(contents)):
        if(contents[i].isdigit()):
            bag=contents[i+1]+" "+contents[i+2]
            holdings.append(bag)
            i+=3
        else:
            i+=1
    return holdings

graph={}
visiting={}
with open('../input.txt','r') as f:
    for line in f:
        line=line.strip()
        count=0
        i=0
        while(count<2):
            if(line[i]==' '):
                count+=1
            i+=1
        i-=1
        container=line[:i]
        remaining=line[i+14:]
        holdings=extractHoldings(remaining)
        graph[container]=holdings
        visiting[container]=0
    f.close()

count=0
flag=0
DFS(graph)
print(count)
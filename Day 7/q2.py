import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def countBags(container):
    if(len(graph[container])==0):
        return 0
    contents=0
    for holding in graph[container]:
        holding=holding.split(' ')
        bagCount=int(holding[0])
        holding=' '.join(holding[1:])
        contents+=bagCount*(1+countBags(holding))
    return contents

def extractHoldings(contents):
    holdings=[]
    contents=contents.split(' ')
    i=0
    while(i<len(contents)):
        if(contents[i].isdigit()):
            bag=contents[i]+" "+contents[i+1]+" "+contents[i+2]
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

count=countBags('shiny gold')
print(count)
import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def update(x,i,seen):
    if(x not in seen):
        seen[x]=[]
    if(len(seen[x])<2):
        seen[x].append(i)
    else:
        seen[x][0],seen[x][1]=seen[x][1],i

def elvesGame(starting, limit):
    game={}
    seen={}
    for i in range(len(starting)):
        seen[starting[i]]=[]

    for i in range(1,len(starting)+1):
        seen[starting[i-1]].append(i)
        game[i]=starting[i-1]

    last=starting[-1]
    i=len(starting)+1
    
    while(i<=limit):
        if(len(seen[last])==1):
            ans=0
        else:
            ans=seen[last][1]-seen[last][0]
        game[i]=ans
        update(ans,i,seen)
        last=game[i]
        i+=1
    return game[limit]

starting = list(map(int,input().split(',')))
print(elvesGame(starting,2020))
print(elvesGame(starting,30000000))
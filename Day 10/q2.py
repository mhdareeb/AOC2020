import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

with open('../input.txt','r') as f:
    adapters=[]
    for line in f:
        adapters.append(int(line.strip()))
    f.close()
    device=max(adapters)+3
    adapters.append(0)
    adapters.append(device)
    adapters=sorted(adapters)
    f.close()

n=len(adapters)
paths=[0]*n
paths[n-1]=1
for i in range(n-2,-1,-1):
    count=0
    adapter=adapters[i]
    for j in range(1,4):
        newadapter=adapter+j
        if(newadapter in adapters[i+1:n]):
            idx=adapters.index(newadapter)
            count+=paths[idx]
    paths[i]=count
    
print(paths[0])
import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def connect(adapter):
    global count
    if(adapter==device):
        count+=1
        return
    for i in range(1,4):
        newadapter=adapter+i
        if newadapter in adapters:
            connect(newadapter)

with open('../input.txt','r') as f:
    adapters=set([])
    for line in f:
        adapters.add(int(line.strip()))
    f.close()
    device=max(adapters)+3
    adapters.add(device)
    f.close()

count=0
connect(0)
print(count)
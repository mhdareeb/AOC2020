import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def binarySearch(sequence,left,right,first,second):
    for char in sequence:
        mid=(left+right)//2
        if(char==first):
            right=mid
        else:
            left=mid+1
    return left

def sigma(n):
    return n*(n+1)//2

ans=0
total=0
start=1023
end=0
with open('../input.txt','r') as f:
    for line in f:
        line=line.strip()
        row=binarySearch(line[:7],0,127,'F','B')
        col=binarySearch(line[7:],0,7,'L','R')
        seatID=row*8+col
        start=min(start,seatID)
        end=max(end,seatID)
        total+=seatID
        ans=max(ans,seatID)
    missing=sigma(end)-sigma(start-1)-total
    print(ans)
    print(missing)
    f.close()
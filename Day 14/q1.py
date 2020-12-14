import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def binary(x,n):
    part=bin(x)[2:]
    return '0'*(n-len(part))+part

def mutate(mask,x):
    n=len(mask)
    binx=binary(x,n)
    result=[char for char in binx]
    for i in range(n):
        if(mask[i]!='X'):
            result[i]=mask[i]
    decimal=int(''.join(result),2)
    return decimal

with open('../input.txt','r') as f:
    total=0
    memory={}
    for line in f:
        line=line.strip()
        if(line[1]=='a'):
            mask=line[7:]
        else:
            start=line.index('[')
            end=line.index(']')
            address=line[start+1:end]
            original=int(line[end+4:])
            mutated=mutate(mask,original)
            if address in memory:
                total-=memory[address]
            memory[address]=mutated
            total+=mutated
    print(total)
    f.close()
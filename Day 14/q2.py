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
        if(mask[i]!='0'):
            result[i]=mask[i]
    return result

def combinations(sequence,i):
    if(i==len(sequence)):
        yield ''.join(sequence)
        return
    if(sequence[i]=='X'):
        sequence[i]='0'
        yield from combinations(sequence,i+1)
        sequence[i]='1'
        yield from combinations(sequence,i+1)
        sequence[i]='X'
    else:
        yield from combinations(sequence,i+1)

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
            original=int(line[start+1:end])
            value=int(line[end+4:])
            mutated=mutate(mask,original)
            mutated_addresses=combinations(mutated,0)
            for address in mutated_addresses:
                if address in memory:
                    total-=memory[address]
                memory[address]=value
                total+=value
    print(total)
    f.close()
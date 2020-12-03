import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def countTrees(right,down):
    count=0
    i=0
    j=0
    while(i<323 and j<31):
        line=forest[i]
        if(line[j]=='#'):
            count+=1
        j=(j+right)%31
        i+=down
    return count

forest=[]
for _ in range(323):
    line=input()
    forest.append(line)

slopes=[(1,1),(3,1),(5,1),(7,1),(1,2)]
ans=1
for slope in slopes:
    trees=countTrees(slope[0],slope[1])
    print(trees)
    ans*=trees
print(ans)
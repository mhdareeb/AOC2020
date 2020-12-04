import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

with open('../input.txt','a') as f:
    f.write('\n')
    f.write('\n')
    f.close()

def isValid(passport):
    if(len(passport)<7):
        return False
    elif(len(passport)==7):
        passport=[val[:val.index(':')] for val in passport]
        if('cid' in passport):
            return False
    return True

with open('../input.txt','r') as f:
    passport=""
    count=0
    for line in f:
        if(line!='\n'):
            passport+=line.strip()+' '
        else:
            passport=passport.strip()
            passport=passport.split(' ')
            if(isValid(passport)):
                count+=1
            passport=""
    print(count)
    f.close()
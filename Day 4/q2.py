import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def isValid(passport):
    data=dict()
    for val in passport:
        idx=val.index(':')
        data[val[:idx]]=val[idx+1:]
    if(len(passport)==7 and 'cid' in data):
        return False
    if(len(data['byr'])!=4 or not data['byr'].isdigit() or int(data['byr'])<1920 or int(data['byr'])>2002):
        return False
    if(len(data['iyr'])!=4 or not data['iyr'].isdigit() or int(data['iyr'])<2010 or int(data['iyr'])>2020):
        return False
    if(len(data['eyr'])!=4 or not data['eyr'].isdigit() or int(data['eyr'])<2020 or int(data['eyr'])>2030):
        return False
    if(data['hgt'][-2:] not in ['cm','in'] or not data['hgt'][:-2].isdigit()):
        return False
    else:
        scale=data['hgt'][-2:]
        height=int(data['hgt'][:-2])
        if(scale=='cm' and (height<150 or height>193)):
            return False
        elif(scale=='in' and (height<59 or height>76)):
            return False
    if(len(data['hcl'])!=7 or data['hcl'][0]!='#'):
        return False
    else:
        for char in data['hcl'][1:]:
            if(ord(char)>=48 and ord(char)<=57):
                continue
            elif(ord(char)>=97 and ord(char)<=102):
                continue
            else:
                return False
    if(data['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']):
        return False
    if(len(data['pid'])!=9 or not data['pid'].isdigit()):
        return False 
    return True

with open('../input.txt','a') as f:
    f.write('\n')
    f.write('\n')
    f.close()

with open('../input.txt','r') as f:
    passport=""
    count=0
    for line in f:
        if(line!='\n'):
            passport+=line.strip()+' '
        else:
            passport=passport.strip()
            passport=passport.split(' ')
            if(len(passport)>=7 and isValid(passport)):
                count+=1
            passport=""
    print(count)
    f.close()
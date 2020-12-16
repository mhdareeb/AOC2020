import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

def removePossible(j):
    for i in unknown:
        if j in matching[i]:
            matching[i].remove(j)

def isValidRule(entry,rule):
    for limits in rule:
        if entry in range(limits[0],limits[1]+1):
            return True
    return False

def allfit(column,ruleNo):
    rule=rules[ruleNo]
    for entry in column:
        if not isValidRule(entry,rule):
            return False
    return True

def findCategory(column):
    possibles=[]
    for j in range(n):
        if allfit(column,j):
            possibles.append(j)
    return possibles

def isValid(value):
    for rule in rules:
        if isValidRule(value,rule):
            return True
    return False

def validTicket(nearby):
    for value in nearby:
        if not isValid(value):
            return False
    return True

with open('../input.txt','r') as f:
    rules=[]
    line=f.readline()
    while line!='\n':
        line=line.strip().split(': ')[1]
        line=line.split(' or ')
        line=[list(map(int,limits.split('-'))) for limits in line]
        rules.append(line)
        line=f.readline()
    line=f.readline()
    myticket=list(map(int,f.readline().strip().split(',')))
    line=f.readline()
    line=f.readline()
    valid=[]
    for nearby in f:
        nearby=list(map(int,nearby.strip().split(',')))  
        if validTicket(nearby):
            valid.append(nearby)
    n=len(rules)
    matching={}
    for i in range(n):
        column_entries=[]
        for ticket in valid:
            column_entries.append(ticket[i])
        matching[i]=findCategory(column_entries)
    unknown=set(range(n))
    while(unknown):
        for i in unknown:
            if(len(matching[i])==1):
                break
        unknown.remove(i)
        removePossible(matching[i][0])
    prod=1
    for i in range(n):
        if matching[i][0] in range(6):
            prod*=myticket[i]    
    print(prod)
    f.close()    
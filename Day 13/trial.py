import os
import sys

if(os.getenv('username')=="Areeb"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

with open('../input.txt','r') as file:
    data = file.read().splitlines()

timestamp = int(data[0])
busses = [int(l) if l != "x" else None for l in data[1].split(",")]

# Part 1

best_bus = None
min_wait_time = float('inf')

for bus in busses:
    if bus:
        wait_time = bus - timestamp % bus
        if min_wait_time > wait_time:
            min_wait_time = wait_time
            best_bus = bus

print(best_bus * min_wait_time)

# Part 2

timestamp = 0

while not all([(timestamp + k) % bus == 0 for k, bus in enumerate(busses) if bus]):
    valid_busses = [bus for k, bus in enumerate(
        busses) if bus and (timestamp + k) % bus == 0]
    prod = 1
    for bus in valid_busses:
        prod *= bus
    print(valid_busses)
    timestamp += prod
    print(timestamp)
print(timestamp)
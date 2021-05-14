import math
f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

TARGET = int(input[0])

# {bus: index}
buses = {}
for index, bus in enumerate(input[1].split(',')):
    if bus != 'x':
        buses[int(bus)] = index

print(buses)
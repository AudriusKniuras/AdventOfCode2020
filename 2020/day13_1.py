import math
f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

TARGET = int(input[0])
buses = [int(bus) for bus in input[1].split(',') if bus != 'x']

def next_departure(bus):
    upper_rounded = math.ceil(TARGET/bus)
    time_diff = bus*upper_rounded - TARGET
    return time_diff

result = [0, TARGET]
for bus in buses:
    time_diff = next_departure(bus)
    if time_diff < result[1]:
        result[1] = time_diff
        result[0] = bus

print(result)
print(result[0] * result[1])
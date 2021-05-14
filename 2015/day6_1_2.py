from time import time
import re

t0 = time()

grid = []
for i in range(1000):
  grid.append([])
  for j in range(1000):
    grid[i].append(0)

actions = {
  'toggle': lambda x: 0 if x == 1 else 1,
  'turn on': lambda x: 1,
  'turn off': lambda x: 0,
}

file = []
with open('input.txt', 'r') as f:
  file = f.readlines()

for line in file:
  instructions = re.findall("(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)", line)
  action, x1, y1, x2, y2 = instructions[0]
  coord = [(x, y) for x in range(int(x1), int(x2) + 1) for y in range(int(y1), int(y2) + 1) ]
  for x, y in coord:
    grid[x][y] = actions[action](grid[x][y])

flattened = [val for sublist in grid for val in sublist]
print(sum(flattened))


t1 = time()

print(f'elapsed time: {t1-t0}')
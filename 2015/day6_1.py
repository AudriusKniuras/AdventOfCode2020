grid = []
for i in range(1000):
  grid.append([])
  for j in range(1000):
    grid[i].append(0)

# start = [a,b], end = [x,z]
def turn_off(start, end):
  curr_start = start[1]
  while start[0] <= end[0]:
    while curr_start <= end[1]:
      grid[start[0]][curr_start] = 0
      curr_start += 1
    start[0] += 1
    curr_start = start[1]
  return grid

def toggle(start, end):
  curr_start = start[1]
  while start[0] <= end[0]:
    while curr_start <= end[1]:
      if grid[start[0]][curr_start] == 1:
        grid[start[0]][curr_start] = 0
      else:
        grid[start[0]][curr_start] = 1
      curr_start += 1
    start[0] += 1
    curr_start = start[1]
  return grid


  while start[0] <= end[0]:
    while start[1] <= end[1]:
      if grid[start[0]][start[1]] == 0:
        grid[start[0]][start[1]] = 1
      else:
        grid[start[0]][start[1]] = 0
      start[1] += 1
    start[0] += 1
  return grid

def turn_on(start, end):
  curr_start = start[1]
  while start[0] <= end[0]:
    while curr_start <= end[1]:
      grid[start[0]][curr_start] = 1
      curr_start += 1
    start[0] += 1
    curr_start = start[1]
  return grid


with open('input.txt', 'r') as f:
  for line in f:
    start1 = int(line.split(',')[0].split(' ')[-1])
    start2 = int(line.split(',')[1].split(' ')[0])

    end1 = int(line.split(',')[1].split(' ')[-1])
    end2 = int(line.split(',')[2].split(' ')[0])
    if 'toggle' in line:
      grid = toggle([start1, start2], [end1, end2])
    elif 'turn on' in line:
      grid = turn_on([start1, start2], [end1, end2])
    elif 'turn off' in line:
      grid = turn_off([start1, start2], [end1, end2])

lit_lights = 0
for i in range(1000):
  for j in range(1000):
    if grid[i][j] == 1:
      lit_lights += 1
print(lit_lights)
# print(grid)

# a = []
# for i in range(4):
#   a.append([])
#   for j in range(4):
#     a[i].append(f'{i} {j}')
# print(a)
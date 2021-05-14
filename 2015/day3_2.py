from collections import Counter

cur_pos_santa = 0+0j
cur_pos_robo = 0+0j
path = []
path.append(cur_pos_santa)
path.append(cur_pos_robo)
directions = {
  '^': 1,
  '>': 1j,
  '<': -1j,
  'v': -1
}

move = 0

with open('input.txt', 'r') as f:
  for line in f:
    for direction in line:
      if move == 0:
        cur_pos_santa += directions[direction]
        path.append(cur_pos_santa)
        move += 1
      else:
        cur_pos_robo += directions[direction]
        path.append(cur_pos_robo)
        move -= 1


count_dict = dict(Counter(path))
output = 0
for key in count_dict:
  if count_dict[key] > 0:
    output += 1
print(output)

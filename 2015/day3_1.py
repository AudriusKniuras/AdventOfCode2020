from collections import Counter

cur_pos = 0+0j
path = []
path.append(cur_pos)
directions = {
  '^': 1,
  '>': 1j,
  '<': -1j,
  'v': -1
}


with open('input.txt', 'r') as f:
  for line in f:
    for direction in line:
      cur_pos += directions[direction]
      path.append(cur_pos)


count_dict = dict(Counter(path))
output = 0
for key in count_dict:
  if count_dict[key] > 0:
    output += 1
print(output)

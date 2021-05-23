from itertools import permutations

with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

stars = []
distances = []
for line in lines:
  s = line.split(' ')
  if s[0] not in stars:
    stars.append(s[0])
  if s[2] not in stars:
    stars.append(s[2])

for line in lines:
  s = line.split(' ')
  distances.append([s[0],s[2],s[4]])

stars_perm = permutations(stars)

calculated_distances = {}
for path in list(stars_perm):
  curr_path_distance = 0
  found = False
  for i,star in enumerate(path):
    if path[-1] != star:
      for distance in distances:
        if star in distance and path[i+1] in distance:
          curr_path_distance += int(distance[2])
  calculated_distances[curr_path_distance] = path

print(max(calculated_distances.keys()))
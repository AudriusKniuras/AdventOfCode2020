total = 0

with open('input.txt', 'r') as f:
  for line in f:
      sides = [int(x) for x in line.split('x')]
      sides.sort()
      total += sides[0]*2 + sides[1]*2 + sides[0]*sides[1]*sides[2]

print(total)
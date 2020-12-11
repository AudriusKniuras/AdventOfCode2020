f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

f.close()

length = len(input[0])
multiplier = 100
slope = []
trees = 0

for index, line in enumerate(input):
  if index == 0:
    continue

  line *= multiplier
  slope.append(3)
  square = line[slope.count(3) * 3]
  if square == '#':
    trees += 1

print(trees)


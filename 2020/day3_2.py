f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

f.close()

length = len(input[0])
multiplier = 100
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]


trees = 0

result = 1

for slope in slopes:
  for index, line in enumerate(input):
    if index == 0:
      continue

    if slope[1] == 2:
      if index % 2 == 1:
        continue

    line *= multiplier

    # line index * right slope
    # if slope 3, 3*1, 3*2...
    if slope[1] == 1:
      square = line[index*slope[0]]
    else:
      square = line[int(index/2)*slope[0]]
    if square == '#':
      trees += 1

  print(trees)
  result *= trees
  trees = 0

print(f'result: {result}')



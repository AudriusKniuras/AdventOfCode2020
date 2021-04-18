f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

f.close()

rules = {}

# if bag not in dict:
# dict[bag] = [contain]
# dict[contain] = []
# if bag in dict:
# dict[bag].append(bag)
# 
count = 0
for line in input:
  bag, contain = line.split('bags contain')

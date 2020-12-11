f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

f.close()

count = 0

for i in input:
  line = i.split()
  req = line[0].split('-')
  letter = line[1].split(':')[0]
  word = line[2]
  letter_count = word.count(letter)
  if letter_count >= int(req[0]) and letter_count <= int(req[1]):
    count += 1

print(count)

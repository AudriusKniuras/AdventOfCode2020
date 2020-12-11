f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

f.close()

count = 0

for i in input:
  line = i.split()
  req1, req2 = line[0].split('-')
  req1 = int(req1) - 1
  req2 = int(req2) - 1
  letter = line[1].split(':')[0]
  word = line[2]

  if word[req1] == letter and word[req2] != letter:
    count +=1
  if word[req1] != letter and word[req2] == letter:
    count +=1


print(count)

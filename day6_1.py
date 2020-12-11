f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]
input.append('')
f.close()

answers = ""
total = 0
for line in input:
  if line != '':
    answers += line
  else:
    count = len(set(answers))
    total += count
    print(count)
    answers = ""

print(total)
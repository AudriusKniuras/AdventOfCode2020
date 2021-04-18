import collections

f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]
input.append('')
f.close()

total = 0
answers = ""
answers_arr = []
for line in input:
  if line != '':
    answers += line
    answers_arr.append(line)
  else:
    count = 0
    unique = set(answers.replace(' ', ''))
    for letter in unique:
      res = [i for i in answers_arr if letter in i]
      if len(res) == len(answers_arr):
        # print(f'letter: {letter} matched in all')
        count += 1

    # print(count)
    total += count
    answers = ""
    answers_arr = []

print(total)
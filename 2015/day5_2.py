arr = []

def pair_twice(s):
  for num,letter in enumerate(s):
    if num+1 < len(s):
       pair = letter + s[num+1]
       if s.count(pair) > 1:
         return True
  return False

def letter_repeat(s):
  for num,letter in enumerate(s):
    if num+2 < len(s):
      three = letter + s[num+1] + s[num+2]
      if three[0] == three[2]:
        return True
  return False

with open('input.txt', 'r') as f:
  for line in f:
    if pair_twice(line) and letter_repeat(line):
      arr.append(line)



print(arr)
print(len(arr))
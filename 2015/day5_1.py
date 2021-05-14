arr = []

def vowel_count(s):
  sum = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
  if sum >= 3:
    return True
  return False

def letter_twice(s):
  for num,letter in enumerate(s):
    if num+1 < len(s):
       if letter == s[num+1]:
         return True
  return False

def bad_letters(s):
  arr = ['ab','cd','pq','xy']
  for i in arr:
    if i in s:
      return False
  return True


with open('input.txt', 'r') as f:
  for line in f:
    if vowel_count(line) and letter_twice(line) and bad_letters(line):
      arr.append(line)



print(arr)
print(len(arr))
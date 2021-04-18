floor = 0

with open("input.txt", "r") as file:
  for line in file:
    for char in line:
      if char == '(':
        floor += 1
      elif char == ')':
        floor -=1

print(floor)

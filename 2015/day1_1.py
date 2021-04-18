floor = 0

with open("input.txt", "r") as file:
  for line in file:
    for index, char in enumerate(line):
      if char == '(':
        floor += 1
      elif char == ')':
        floor -=1
      if floor == -1:
        print(f"index: {index} ")
        break


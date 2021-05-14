from numpy import uint16

instructions = {
  'and': lambda x,y: x&y,
  'or': lambda x,y: x|y,
  'lshift': lambda x,y: x << y,
  'rshift': lambda x,y: x >> y,
  'not': lambda x: ~x
}

values = {}

lines = []
with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

unresolved = len(lines)
resolved_lines = []


def and_funct(a, b, result):
  if a.isnumeric() or b.isnumeric():
    if a in values:
      values[result] = instructions['and'](b, values[a])
    elif b in values:
      values[result] = instructions['and'](a, values[b])
    else:
      return False
  elif (a in values) and (b in values):
    values[result] = instructions['and'](values[a], values[b])
  else:
    return False
  return True

def or_funct(a, b, result):
  if a.isnumeric() or b.isnumeric():
    if a in values:
      values[result] = instructions['or'](b, values[a])
    elif b in values:
      values[result] = instructions['or'](a, values[b])
    else:
      return False
  elif (a in values) and (b in values):
    values[result] = instructions['and'](values[a], values[b])
  else:
    return False
  return True


while unresolved > 0:
  for line in lines:
    line = line.split(' ')
    if 'AND' in line:
      if and_funct(line[0], line[2], line[-1]):
        resolved_lines.append(line)
        unresolved -= 1
    elif 'OR' in line:
      if or_funct(line[0], line[2], line[-1]):
        resolved_lines.append(line)
        unresolved -= 1
  # TODO:
  lines = lines - unresolved
      


    



# with open('input.txt', 'r') as f:
#   for line in f:
#     line = line.strip().split(' ')
#     if 'AND' in line:
#       values[line[-1]] = instructions['and'](values[line[0]], values[line[2]])
#     elif 'OR' in line:
#       values[line[-1]] = instructions['or'](values[line[0]], values[line[2]])
#     elif 'LSHIFT' in line:
#       values[line[-1]] = instructions['lshift'](values[line[0]], int(line[2]))
#     elif 'RSHIFT' in line:
#       values[line[-1]] = instructions['rshift'](values[line[0]], int(line[2]))
#     elif 'NOT' in line:
#       values[line[-1]] = instructions['not'](values[line[1]])
#     else:
#       values[line[-1]] = uint16(line[0])

# print(values)
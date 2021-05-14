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


def convert_uint16(num):
  try:
    return uint16(num)
  except:
    return num

def check_numeric(num):
  if 

def and_funct(a, b, result):
  a = convert_uint16(a)
  b = convert_uint16(b)
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
  a = convert_uint16(a)
  b = convert_uint16(b)
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

def lshift_funct(a, b, result):
  a = convert_uint16(a)
  b = convert_uint16(b)
  if a in values:
    values[result] = instructions['lshift'](values[a], b)
    return True
  return False

def rshift_funct(a, b, result):
  a = convert_uint16(a)
  b = convert_uint16(b)
  if a in values:
    values[result] = instructions['rshift'](values[a], b)
    return True
  return False

def not_funct(a, result):
  a = convert_uint16(a)
  if a in values:
    values[result] = instructions['not'](values[a])
    return True
  return False

def assign_funct(a, result):
  a = convert_uint16(a)
  if a.isnumeric():
    values[result] = a
    return True
  else:
    if a in values:
      values[result] = values[a]
      return True
  return False

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
    elif 'LSHIFT' in line:
      if lshift_funct(line[0], line[2], line[-1]):
        resolved_lines.append(line)
        unresolved -= 1
    elif 'RSHIFT' in line:
      if rshift_funct(line[0], line[2], line[-1]):
        resolved_lines.append(line)
        unresolved -= 1
    elif 'NOT' in line:
      if not_funct(line[1], line[-1]):
        resolved_lines.append(line)
        unresolved -= 1
    else:
      if assign_funct(line[0], line[-1]):
        resolved_lines.append(line)
        unresolved -= 1

  tmp_lines = [line for line in lines if line not in resolved_lines]
  lines = tmp_lines.copy()
      


    



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
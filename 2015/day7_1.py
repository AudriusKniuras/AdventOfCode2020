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


def and_funct(a, b, result):
  a = convert_uint16(a)
  b = convert_uint16(b)
  if type(a) != str or type(b) != str:
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
  if type(a) != str or type(b) != str:
    if a in values:
      values[result] = instructions['or'](b, values[a])
    elif b in values:
      values[result] = instructions['or'](a, values[b])
    else:
      return False
  elif (a in values) and (b in values):
    values[result] = instructions['or'](values[a], values[b])
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
  if type(a) != str:
    values[result] = a
    return True
  else:
    if a in values:
      values[result] = values[a]
      return True
  return False

while len(resolved_lines) != unresolved:
  for line in lines:
    org_line = line
    line = line.split(' ')
    if 'AND' in line:
      if and_funct(line[0], line[2], line[-1]):
        resolved_lines.append(org_line)
    elif 'OR' in line:
      if or_funct(line[0], line[2], line[-1]):
        resolved_lines.append(org_line)
    elif 'LSHIFT' in line:
      if lshift_funct(line[0], line[2], line[-1]):
        resolved_lines.append(org_line)
    elif 'RSHIFT' in line:
      if rshift_funct(line[0], line[2], line[-1]):
        resolved_lines.append(org_line)
    elif 'NOT' in line:
      if not_funct(line[1], line[-1]):
        resolved_lines.append(org_line)
    else:
      if assign_funct(line[0], line[-1]):
        resolved_lines.append(org_line)
  tmp_lines = [line for line in lines if line not in resolved_lines]
  # print(resolved_lines)
  lines = tmp_lines
      
print(values)

    



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
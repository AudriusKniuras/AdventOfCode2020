f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

f.close()

results = []
max_result = 0
for row in input:
  lower_half = 0
  upper_half = 128
  upper_num = 8
  lower_num = 0
  for letter in row:
    mid_point = (upper_half - lower_half) // 2
    if letter == 'F':
      upper_half -= mid_point
    if letter == 'B':
      lower_half += mid_point
    mid_num = (upper_num - lower_num) // 2
    if letter == 'R':
      lower_num += mid_num
    if letter == 'L':
      upper_num -= mid_num
  result = lower_half * 8 + lower_num
  results.append(result)
  if result > max_result:
    max_result = result

print(max_result)

# ---------- part 2
results.sort()
expected = 34
for res in results:
  expected += 1
  if res != expected:
    print(f'seat found: {expected}')
    break
total = 0

with open('input.txt', 'r') as f:
  for line in f:
    d = [int(x) for x in line.split('x')]
    a = d[0]*d[1]
    b = d[1]*d[2]
    c = d[0]*d[2]
    m = min(a,b,c)
    total += 2 * (a+b+c) + m

print(total)
with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

sum = 0
sum2 = 0
for line in lines:
    total = len(line)
    repl_total = len(eval(line))
    sum += total - repl_total

    line2 = line.replace('\\', '\\\\').replace('"', '\\"')
    sum2 += len(line2) - len(line)


print(sum2)

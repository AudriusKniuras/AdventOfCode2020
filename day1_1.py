f = open("input.txt", "r")

numbers = [int(x) for x in f.read().split('\n')]

f.close()

for num in numbers:
  for n in numbers:
    if num+n == 2020:
      print(f"n: {n}, num: {num}")

print(633*1387)
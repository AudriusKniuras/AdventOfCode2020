f = open("input.txt", "r")

numbers = [int(x) for x in f.read().split('\n')]

f.close()

for num in numbers:
  for n in numbers:
    for d in numbers:
      if num+n+d == 2020:
        print(f"n: {n}, num: {num}, d: {d}")

print(264*889*867)
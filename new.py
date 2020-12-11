import ast

f = open("1output", "r")

# x = ast.literal_eval(f.read())

input = [ast.literal_eval(x) for x in f.read().split('\n')]


f.close()
# k,v = input[0][0]
# print(k)
# print(v)
# print(input[0][0])
print(input[0])
for passport in input:
  for k,v in passport:
    if k == "pid":
      print(v)
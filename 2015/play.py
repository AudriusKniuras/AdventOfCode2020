# map:

def addition(n):
    return n+n

numbers = (1,2,3,4)
result = map(addition, numbers)
print(list(result)) # [2, 4, 6, 8]

result = map(lambda x: x+x, numbers)
print(list(result)) # [2, 4, 6, 8]

result = map(lambda x,y: x+y, [1,2,3], [4,5,6])
print(list(result)) # [5, 7, 9]
f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

f.close()

PREAMBLE = 25

length = len(input)

for i in range(PREAMBLE, length):
    found = False
    numbers = input[i-PREAMBLE:i]
    # print(f'{numbers}, {input[i]}')
    for index1, n1 in enumerate(numbers):
        sum = 0
        for index2, n2 in enumerate(numbers):
            if index2 <= index1:
                continue
            else:
                sum = int(n1) + int(n2)
                # print(f'sum: {sum}')
            if sum == int(input[i]):
                found = True
                break
        if found:
            break
        
    if not found:
        print(f'{input[i]} not found')
        break

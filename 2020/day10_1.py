f = open("input.txt", "r")

input = [int(x) for x in f.read().split('\n')]

f.close()

STEP = 3

# def find_next(step, current_number):
#     results = []
#     for number in input:
#         if (number <= current_number + step) and (number > current_number):
#             results.append(number)
#     return min(results)

# input = input.sort()

# current_number = 0

# for number in input:
    
diff_1 = 0
diff_3 = 0
input.sort()
prev_number = 0
for number in input:
    if (number - prev_number) == 3:
        diff_3 += 1
    elif (number - prev_number) == 1:
        diff_1 += 1
    prev_number = number
diff_3 += 1
print(diff_1)
print(diff_3)

answer = diff_1 * diff_3
print(f'answer: {answer}')
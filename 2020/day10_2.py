f = open("input.txt", "r")

input = [int(x) for x in f.read().split('\n')]

f.close()

input.sort()

STEP = 3

input = [1,2,4,5]

# def find_next(step, current_number):
#     results = []
#     for number in input:
#         if (number <= current_number + step) and (number > current_number):
#             results.append(number)
#     return min(results)

# input = input.sort()

# current_number = 0

# for number in input:
    
# diff_1 = 0
# diff_3 = 0
# input.sort()
# prev_number = 0
# for number in input:
#     if (number - prev_number) == 3:
#         diff_3 += 1
#     elif (number - prev_number) == 1:
#         diff_1 += 1
#     prev_number = number
# diff_3 += 1
# print(diff_1)
# print(diff_3)

# answer = diff_1 * diff_3
# print(f'answer: {answer}')



# 1. rasti kiek skaicius turi keliu
# 2. Eiti i pirma kelia, surasti kiek kitas skaicius turi keliu, eiti i pirma kelia....
# 3. Gale isprintinamas kelias
# 4. Eina i sekanti skaiciu nuo pradziu

def find_paths(index, number):
    paths = []
    index += 1
    while index < len(input):
        if input[index] - number < 4:
            paths.append(input[index])
        else:
            break
        index += 1
    return paths


print(find_paths(3, 5))
        
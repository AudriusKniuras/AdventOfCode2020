f = open("input.txt", "r")

input = [int(x) for x in f.read().split('\n')]

f.close()

# TARGET = 127
TARGET = 177777905

length = len(input)

def add_numbers(sum, index):
    added_numbers.append(input[index])
    sum += input[index]
    if sum > TARGET:
        return False
    if sum == TARGET:
        print(f'FOUND: {added_numbers}')
        return True
    add_numbers(sum, index + 1)  




for index, number in enumerate(input):
    sum = 0
    added_numbers = []
    if (add_numbers(sum, index)):
        added_numbers.sort()
        answer = added_numbers[0] + added_numbers[-1]
        # doesnt work correctly, adds 177777905 + 177777905
        print(f'ANSWER: {answer}')
        break

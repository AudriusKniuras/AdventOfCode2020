f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

f.close()

def parse_instruction(instruction):
    instruction = instruction.split(' ')
    # acc, nop, jpm
    ins1 = instruction[0]
    # + or -
    ins2 = instruction[1][0]
    # number
    ins3 = int(instruction[1][1:])
    return [ins1, ins2, ins3]

def f_jmp(instruction, accumulator, position):
    instruction = parse_instruction(instruction)
    if instruction[1] == "+":
        position += instruction[2]
    elif instruction[1] == "-":
        position -= instruction[2]
    return accumulator, position

def f_acc(instruction, accumulator, position):
    instruction = parse_instruction(instruction)
    if instruction[1] == "+":
        accumulator += instruction[2]
    elif instruction[1] == "-":
        accumulator -= instruction[2]
    position += 1
    return accumulator, position

def f_nop(instruction, accumulator, position):
    position += 1
    return accumulator, position


position = 0
changed_positions = []

for index, instruction in enumerate(input):
    instructions = input[:]
    if "nop" in instruction:
        ins = instruction.split(' ')
        if ins[1] == "+0" or ins[1] == "-0":
            continue
        instructions[index] = instructions[index].replace('nop', 'jmp')
    elif "jmp" in instruction:
        instructions[index] = instructions[index].replace('jmp', 'nop')
        

    accumulator, position = 0, 0
    instruction_order = []

    while True:
        if position in instruction_order:
            # print(accumulator)
            break
        elif position >= len(instructions):
            print(f'position > len, accumulator: {accumulator}')
            break
        else:
            instruction_order.append(position)

        instruction = instructions[position]
        # print(f'instruction: {instruction}')
        # print(f'position: {position}')

        if "acc" in instruction:
            accumulator, position = f_acc(instruction, accumulator, position)
        if "jmp" in instruction:
            accumulator, position = f_jmp(instruction, accumulator, position)
        if "nop" in instruction:
            accumulator, position = f_nop(instruction, accumulator, position)
        
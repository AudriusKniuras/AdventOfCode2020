f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

f.close()

pos = {'N': 0, 'E': 0}

curr_pos = 'E'


def move_forward(pos, curr_pos, steps):
    if curr_pos == 'N':
        pos['N'] += steps
    elif curr_pos == 'S':
        pos['N'] -= steps
    elif curr_pos == 'E':
        pos['E'] += steps
    elif curr_pos == 'W':
        pos['E'] -= steps
    return pos

def move(pos, direction, steps):
    if direction == 'N':
        pos['N'] += steps
    elif direction == 'S':
        pos['N'] -= steps
    elif direction == 'E':
        pos['E'] += steps
    elif direction == 'W':
        pos['E'] -= steps
    return pos

def turn(curr_pos, direction, degrees):
    positions = 2*('E', 'S', 'W', 'N')
    positions_rev = positions[::-1]
  
    
    steps = degrees // 90

    if direction == 'R':
        index = positions.index(curr_pos)
        curr_pos = positions[index+steps]
    elif direction == 'L':
        index = positions_rev.index(curr_pos)
        curr_pos = positions_rev[index+steps]
    return curr_pos

def solve_part1(pos):
    return abs(pos['N']) + abs(pos['E'])

for instr in input:
    if instr[0] == 'F':
        pos = move_forward(pos, curr_pos, int(instr[1:]))
    elif instr[0] in ['N', 'S', 'E', 'W']:
        pos = move(pos, instr[0], int(instr[1:]))
    elif instr[0] in ['L', 'R']:
        curr_pos = turn(curr_pos, instr[0], int(instr[1:]))


print(pos)
result = solve_part1(pos)
print(result)
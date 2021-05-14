f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

f.close()

wayp_pos = {'N': 1, 'E': 10}
ship_pos = {'N': 0, 'E': 0}

curr_pos = 'E'


def move_forward(ship_pos, wayp_pos, steps):
    ship_pos['N'] += wayp_pos['N'] * steps
    ship_pos['E'] += wayp_pos['E'] * steps
    return ship_pos

def move(wayp_pos, direction, steps):
    if direction == 'N':
        wayp_pos['N'] += steps
    elif direction == 'S':
        wayp_pos['N'] -= steps
    elif direction == 'E':
        wayp_pos['E'] += steps
    elif direction == 'W':
        wayp_pos['E'] -= steps
    return wayp_pos

def turn(wayp_pos, direction, degrees):
    steps = degrees // 90
    old_pos = wayp_pos.copy()

    if direction == 'R':
        if steps == 1:
            wayp_pos['E'] = old_pos['N']
            wayp_pos['N'] = -old_pos['E']
        if steps == 2:
            wayp_pos['E'] = -old_pos['E']
            wayp_pos['N'] = -old_pos['N']
        if steps == 3:
            wayp_pos['E'] = -old_pos['N']
            wayp_pos['N'] = old_pos['E']
    elif direction == 'L':
        if steps == 1:
            wayp_pos['E'] = -old_pos['N']
            wayp_pos['N'] = old_pos['E']
        if steps == 2:
            wayp_pos['E'] = -old_pos['E']
            wayp_pos['N'] = -old_pos['N']
        if steps == 3:
            wayp_pos['E'] = old_pos['N']
            wayp_pos['N'] = -old_pos['E']

    return wayp_pos

def solve_part1(ship_pos):
    return abs(ship_pos['N']) + abs(ship_pos['E'])

for instr in input:
    if instr[0] == 'F':
        ship_pos = move_forward(ship_pos, wayp_pos, int(instr[1:]))
        print(f'ship_pos: {ship_pos}')
    elif instr[0] in ['N', 'S', 'E', 'W']:
        wayp_pos = move(wayp_pos, instr[0], int(instr[1:]))
        print(f'wayp_pos: {wayp_pos}')
    elif instr[0] in ['L', 'R']:
        wayp_pos = turn(wayp_pos, instr[0], int(instr[1:]))
        print(f'wayp_pos: {wayp_pos}')


print(f'wayp_pos: {wayp_pos}')
print(f'ship_pos: {ship_pos}')
result = solve_part1(ship_pos)
print(result)
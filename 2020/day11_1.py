import copy

f = open("input.txt", "r")

input = []
for line in f:
    arr = [x for x in line]
    if '\n' in arr:
        arr.remove('\n')
    input.append(arr)

f.close()

# safe list get
def slg(l, index1, index2):
    if index1 < 0 or index2 < 0:
        return 0
    try:
        return l[index2][index1]
    except IndexError:
        return 0

def find_adj(l, x, y):
    neighbors = [slg(l,x-1,y-1), slg(l,x,y-1), slg(l,x+1,y-1), slg(l,x-1,y), slg(l,x+1,y), slg(l,x-1,y+1), slg(l,x,y+1), slg(l,x+1,y+1)]
    neighbors = [x for x in neighbors if x != 0]
    return neighbors

def count_occupied(array):
    count = 0
    for line in array:
        for element in line:
            if element == '#':
                count += 1
    return count


prev_array = copy.deepcopy(input)

changes = True
while changes == True:
    new_array = copy.deepcopy(prev_array)
    for y, line in enumerate(prev_array):
        for x, element in enumerate(line):
            # if element != '.':
            neighbors = find_adj(prev_array, x, y)
            # print(f'x: {x}, y: {y}, {neighbors}, curr element {prev_array[y][x]}')
            if prev_array[y][x] == 'L':
                if neighbors.count('#') == 0:
                    new_array[y][x] = '#'
            elif prev_array[y][x] == '#':
                if neighbors.count('#') > 3:
                    new_array[y][x] = 'L'
    if new_array != prev_array:
        # print(new_array)
        # print('-----------------')
        prev_array = copy.deepcopy(new_array)
    else:
        changes = False
        occupied = count_occupied(new_array)
        print(f'Occupied: {occupied}')





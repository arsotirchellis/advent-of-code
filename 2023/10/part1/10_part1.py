from pathlib import Path

path = Path(__file__).parent / "../input.txt"

with open(path, "r") as file:
    contents = file.read()

lines = [x for x in contents.split("\n")]

matrix = []

start = (0, 0)
for i, line in enumerate(lines):
    matrix.append([])
    for j, char in enumerate(line):
        matrix[i].append(char)
        if char == 'S':
            start = (i, j)

allowed_moves = {
    '7': {'L', 'D'},
    'F': {'R', 'D'},
    'L': {'U', 'R'},
    'J': {'L', 'U'},
    '-': {'L', 'R'},
    '|': {'U', 'D'},
    '.': {}
}

path = []
came_from = ''
pointer = (start[0], start[1])
path.append(pointer)

if 'D' in allowed_moves[matrix[pointer[0]-1][pointer[1]]]:
    pointer = (pointer[0]-1, pointer[1])
    came_from = 'U'
elif 'U' in allowed_moves[matrix[pointer[0]+1][pointer[1]]]:
    pointer = (pointer[0]+1, pointer[1])
    came_from = 'D'
elif 'L' in allowed_moves[matrix[pointer[0]][pointer[1]-1]]:
    pointer = (pointer[0], pointer[1]-1)
    came_from = 'R'
elif 'R' in allowed_moves[matrix[pointer[0]][pointer[1]+1]]:
    pointer = (pointer[0], pointer[1]+1)
    came_from = 'L'

while True:
    path.append(pointer)
    current = matrix[pointer[0]][pointer[1]]
    # print(current)
    if pointer[0] == start[0] and pointer[1] == start[1]:
        break
    
    if came_from != 'L' and 'L' in allowed_moves[current]:
        pointer = (pointer[0], pointer[1]-1)
        came_from = 'R'
        continue
    if came_from != 'R' and 'R' in allowed_moves[current]:
        pointer = (pointer[0], pointer[1]+1)
        came_from = 'L'
        continue
    if came_from != 'U' and 'U' in allowed_moves[current]:
        pointer = (pointer[0]-1, pointer[1])
        came_from = 'D'
        continue
    if came_from != 'D' and 'D' in allowed_moves[current]:
        pointer = (pointer[0]+1, pointer[1])
        came_from = 'U'
        continue

print((len(path)-1)/2)
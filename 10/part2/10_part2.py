from pathlib import Path
import pprint

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

path_dict = {}
came_from = ''
pointer = (start[0], start[1], '', '')

if 'D' in allowed_moves[matrix[pointer[0]-1][pointer[1]]]:
    pointer = (pointer[0], pointer[1], '', 'U')
    path_dict[(pointer[0], pointer[1])] = pointer

    came_from = 'D'
    pointer = (pointer[0]-1, pointer[1], came_from, '')
    path_dict[(pointer[0], pointer[1])] = pointer
elif 'U' in allowed_moves[matrix[pointer[0]+1][pointer[1]]]:
    pointer = (pointer[0], pointer[1], '', 'D')
    path_dict[(pointer[0], pointer[1])] = pointer

    came_from = 'U'
    pointer = (pointer[0]+1, pointer[1], came_from, '')
    path_dict[(pointer[0], pointer[1])] = pointer
elif 'L' in allowed_moves[matrix[pointer[0]][pointer[1]-1]]:
    pointer = (pointer[0], pointer[1], '', 'R')
    path_dict[(pointer[0], pointer[1])] = pointer

    came_from = 'L'
    pointer = (pointer[0], pointer[1]-1, came_from, '')
    path_dict[(pointer[0], pointer[1])] = pointer
elif 'R' in allowed_moves[matrix[pointer[0]][pointer[1]+1]]:
    pointer = (pointer[0], pointer[1], '', 'L')
    path_dict[(pointer[0], pointer[1])] = pointer

    came_from = 'R'
    pointer = (pointer[0], pointer[1]+1, came_from, '')
    path_dict[(pointer[0], pointer[1])] = pointer

while True:
    current = matrix[pointer[0]][pointer[1]]
    if pointer[0] == start[0] and pointer[1] == start[1]:
        pointer = path_dict[(pointer[0], pointer[1])]
        went_to = pointer[3]
        pointer = (pointer[0], pointer[1], came_from, went_to)
        path_dict[(pointer[0], pointer[1])] = pointer
        break

    if came_from != 'L' and 'L' in allowed_moves[current]:
        went_to = 'L'
        pointer = (pointer[0], pointer[1], came_from, went_to)
        path_dict[(pointer[0], pointer[1])] = pointer

        came_from = 'R'
        pointer = (pointer[0], pointer[1]-1, came_from, '')
        continue
    if came_from != 'R' and 'R' in allowed_moves[current]:
        went_to = 'R'
        pointer = (pointer[0], pointer[1], came_from, went_to)
        path_dict[(pointer[0], pointer[1])] = pointer

        came_from = 'L'
        pointer = (pointer[0], pointer[1]+1, came_from, '')
        continue
    if came_from != 'U' and 'U' in allowed_moves[current]:
        went_to = 'U'
        pointer = (pointer[0], pointer[1], came_from, went_to)
        path_dict[(pointer[0], pointer[1])] = pointer

        came_from = 'D'
        pointer = (pointer[0]-1, pointer[1], came_from, '')
        continue
    if came_from != 'D' and 'D' in allowed_moves[current]:
        went_to = 'D'
        pointer = (pointer[0], pointer[1], came_from, went_to)
        path_dict[(pointer[0], pointer[1])] = pointer

        came_from = 'U'
        pointer = (pointer[0]+1, pointer[1], came_from, '')
        continue

sum = 0
for row_index in range(len(matrix)):
    searching = False
    up_to_down = False
    down_to_up = False
    for col_index in range(len(matrix[row_index])):
        if (row_index, col_index) in path_dict:
            pointer = path_dict[(row_index, col_index)]
            char = matrix[row_index][col_index]
            came_from = pointer[2]
            went_to = pointer[3]

            # D -> U for |
            if came_from == 'D' and went_to == 'U':
                searching = not searching
                down_to_up = False
                up_to_down = False
                continue
            # U -> D for |
            if came_from == 'U' and went_to == 'D':
                searching = not searching
                down_to_up = False
                up_to_down = False
                continue

            # Had a trending state and went to the same direction
            # I dont care about L and R
            if (went_to == 'U' or came_from == 'U') and down_to_up:
                searching = not searching
                down_to_up = False
                up_to_down = False
                continue
            if (went_to == 'D' or came_from == 'D') and up_to_down:
                searching = not searching
                down_to_up = False
                up_to_down = False
                continue

            # State initiators
            if not down_to_up and (went_to == 'D' or came_from == 'D'):
                down_to_up = True
                up_to_down = False
                continue

            if not up_to_down and (went_to == 'U' or came_from == 'U'):
                down_to_up = False
                up_to_down = True
                continue

            # Reset states if it goes to the same direction with the state
            if up_to_down and (came_from == 'U' or went_to == 'U'):
                down_to_up = False
                up_to_down = False
                continue
            if down_to_up and (came_from == 'D' or went_to == 'D'):
                down_to_up = False
                up_to_down = False
                continue

        else:  # not in path
            if searching:
                sum += 1
                matrix[row_index][col_index] = 'X'
            else:
                matrix[row_index][col_index] = ' '

print(sum)

for matrix_row in matrix:
    print(matrix_row)

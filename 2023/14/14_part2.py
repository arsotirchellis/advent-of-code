from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, "r") as file:
    contents = file.read()
lines = [x for x in contents.split("\n")]

matrix = []
for line in lines:
    line = line.strip()
    if line:
        matrix.append(list(line))


def roll_rock_upwards(matrix, i, j):
    if matrix[i][j] != "O":
        return matrix

    for ii in range(i-1, -1, -1):
        if matrix[ii][j] == ".":
            matrix[ii][j] = "O"
            matrix[ii+1][j] = "."
        else:
            break

    return matrix


def roll_rock_downwards(matrix, i, j):
    if matrix[i][j] != "O":
        return matrix

    for ii in range(i+1, len(matrix)):
        if matrix[ii][j] == ".":
            matrix[ii][j] = "O"
            matrix[ii-1][j] = "."
        else:
            break

    return matrix


def roll_rock_left(matrix, i, j):
    if matrix[i][j] != "O":
        return matrix

    for jj in range(j-1, -1, -1):
        if matrix[i][jj] == ".":
            matrix[i][jj] = "O"
            matrix[i][jj+1] = "."
        else:
            break

    return matrix


def roll_rock_right(matrix, i, j):
    if matrix[i][j] != "O":
        return matrix

    for jj in range(j+1, len(matrix[i])):
        if matrix[i][jj] == ".":
            matrix[i][jj] = "O"
            matrix[i][jj-1] = "."
        else:
            break

    return matrix


def hash_matrix(matrix):
    return hash(tuple(tuple(row) for row in matrix))


def tilt_platform_on_north(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "O":
                matrix = roll_rock_upwards(matrix, i, j)

    return matrix


def tilt_platform_on_south(matrix):
    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "O":
                matrix = roll_rock_downwards(matrix, i, j)

    return matrix


def tilt_platform_on_west(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "O":
                matrix = roll_rock_left(matrix, i, j)

    return matrix


def tilt_platform_on_east(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1, -1, -1):
            if matrix[i][j] == "O":
                matrix = roll_rock_right(matrix, i, j)

    return matrix


def calculate_load(matrix):
    load = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "O":
                load += len(matrix) - i

    return load


memory = {}
itterations = 1000000000
use_memory = True
i = -1
while i < itterations:
    i += 1

    matrix = tilt_platform_on_north(matrix)
    matrix = tilt_platform_on_west(matrix)
    matrix = tilt_platform_on_south(matrix)
    matrix = tilt_platform_on_east(matrix)
    if use_memory:
        matrix_hash = hash_matrix(matrix)
        if matrix_hash not in memory:
            memory[matrix_hash] = [i]
        else:
            memory[matrix_hash].append(i)
            if len(memory[matrix_hash]) > 2:
                loop_length = memory[matrix_hash][1] - memory[matrix_hash][0]
                itterations_left = (itterations-i) % loop_length
                i = itterations - itterations_left + 1
                use_memory = False
                continue

print(calculate_load(matrix))

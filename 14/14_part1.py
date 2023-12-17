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


def calculate_load(matrix):
    load = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "O":
                load += len(matrix) - i

    return load


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "O":
            matrix = roll_rock_upwards(matrix, i, j)

print(calculate_load(matrix))

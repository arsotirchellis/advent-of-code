from pathlib import Path
import pprint
import math

path = Path(__file__).parent / "../input.txt"
with open(path, "r") as file:
    contents = file.read()
lines = [x for x in contents.split("\n")]
matrix = [[char for char in line] for line in lines]

def expand_universe(matrix) -> list:
    expand_rows = []
    for i, row in enumerate(matrix):
        if all([x == "." for x in row]):
            expand_rows.append(i)
    for i,row in enumerate(expand_rows):
        matrix.insert(row+i, ["." for _ in range(len(matrix[0]))])
    expand_cols = []
    for i, col in enumerate(zip(*matrix)):
        if all([x == "." for x in col]):
            expand_cols.append(i)
    for i, col in enumerate(expand_cols):
        for row in matrix:
            row.insert(col+i, ".")

    return matrix

matrix = expand_universe(matrix)

class Galaxy:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def distance(self, other):
        return abs(self.row - other.row) + abs(self.col - other.col)

galaxies = []
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == "#":
            galaxies.append(Galaxy(i,j))

distances_sum = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies), 1):
            distances_sum += galaxies[i].distance(galaxies[j])
print(distances_sum)
from pathlib import Path
import pprint
import math

path = Path(__file__).parent / "../input.txt"
with open(path, "r") as file:
    contents = file.read()
lines = [x for x in contents.split("\n")]
matrix = [[char for char in line] for line in lines]

expanded_rows = []
for g1, row in enumerate(matrix):
    if all([x == "." for x in row]):
        expanded_rows.append(g1)
expanded_cols = []
for g1, col in enumerate(zip(*matrix)):
    if all([x == "." for x in col]):
        expanded_cols.append(g1)

class Galaxy:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def distance(self, other):
        return 

galaxies = []
for g1, row in enumerate(matrix):
    for g2, col in enumerate(row):
        if col == "#":
            galaxies.append(Galaxy(g1,g2))

increase = 1000000
distances_sum = 0
for g1 in range(len(galaxies)):
    for g2 in range(g1+1, len(galaxies), 1):
            a_galaxy_row = galaxies[g1].row
            a_galaxy_col = galaxies[g1].col
            b_galaxy_row = galaxies[g2].row
            b_galaxy_col = galaxies[g2].col
            for expanded_row in expanded_rows:
                if (galaxies[g1].row < expanded_row and expanded_row < galaxies[g2].row ):
                    b_galaxy_row += increase-1
                if (galaxies[g2].row < expanded_row and expanded_row < galaxies[g1].row):
                    a_galaxy_row += increase-1
            for expanded_col in expanded_cols:
                if (galaxies[g1].col < expanded_col and expanded_col < galaxies[g2].col ):
                    b_galaxy_col += increase-1
                if (galaxies[g2].col < expanded_col and expanded_col < galaxies[g1].col ):
                    a_galaxy_col += increase-1

            distances_sum += abs(a_galaxy_row - b_galaxy_row) + abs(a_galaxy_col - b_galaxy_col)
print(distances_sum)
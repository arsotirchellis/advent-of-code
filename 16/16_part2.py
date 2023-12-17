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


def beam(i, j, direction):
    def move(i, j, from_direction):
        if i < 0 or i > len(matrix) - 1 or j < 0 or j > len(matrix[0]) - 1:
            return []

        energized.add((i, j))

        symbol = matrix[i][j]
        if symbol == '.':
            if from_direction == 'L':
                return [(i, j + 1, 'R')]
            if from_direction == 'R':
                return [(i, j - 1, 'L')]
            if from_direction == 'U':
                return [(i + 1, j, 'D')]
            if from_direction == 'D':
                return [(i - 1, j, 'U')]
        if symbol == '/':
            if from_direction == 'L':
                return [(i - 1, j, 'U')]
            if from_direction == 'R':
                return [(i + 1, j, 'D')]
            if from_direction == 'U':
                return [(i, j - 1, 'L')]
            if from_direction == 'D':
                return [(i, j + 1, 'R')]
        if symbol == '\\':
            if from_direction == 'L':
                return [(i + 1, j, 'D')]
            if from_direction == 'R':
                return [(i - 1, j, 'U')]
            if from_direction == 'U':
                return [(i, j + 1, 'R')]
            if from_direction == 'D':
                return [(i, j - 1, 'L')]
        if symbol == '-':
            if from_direction == 'L':
                return [(i, j + 1, 'R')]
            if from_direction == 'R':
                return [(i, j - 1, 'L')]
            if from_direction == 'U':
                return [(i, j - 1, 'L'), (i, j + 1, 'R')]
            if from_direction == 'D':
                return [(i, j - 1, 'L'), (i, j + 1, 'R')]
        if symbol == '|':
            if from_direction == 'L':
                return [(i - 1, j, 'U'), (i + 1, j, 'D')]
            if from_direction == 'R':
                return [(i - 1, j, 'U'), (i + 1, j, 'D')]
            if from_direction == 'U':
                return [(i + 1, j, 'D')]
            if from_direction == 'D':
                return [(i - 1, j, 'U')]

    energized = set()
    beams = {(i, j, direction)}
    worked_beams = set()

    while len(beams) > 0:
        current_beam = beams.pop()

        if current_beam in worked_beams:
            continue
        worked_beams.add(current_beam)

        i, j, direction = current_beam
        while True:
            next_positions = []
            if direction == 'L':
                next_positions = move(i, j, 'R')
            if direction == 'R':
                next_positions = move(i, j, 'L')
            if direction == 'U':
                next_positions = move(i, j, 'D')
            if direction == 'D':
                next_positions = move(i, j, 'U')

            if len(next_positions) == 0:
                break
            elif len(next_positions) == 1:
                i, j, direction = next_positions[0]
                continue
            else:
                beams.add(next_positions[0])
                beams.add(next_positions[1])
                break

    return len(energized)


max = 0
for j in range(len(matrix[0])):
    energized = beam(0, j, 'D')
    if energized > max:
        max = energized
for j in range(len(matrix[0])):
    energized = beam(len(matrix) - 1, j, 'U')
    if energized > max:
        max = energized
for i in range(len(matrix)):
    energized = beam(i, 0, 'R')
    if energized > max:
        max = energized
for i in range(len(matrix)):
    energized = beam(i, len(matrix[0]) - 1, 'L')
    if energized > max:
        max = energized

print(max)

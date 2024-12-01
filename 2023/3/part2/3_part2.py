from pathlib import Path

path = Path(__file__).parent / "./input.txt"

with open(path, "r") as file:
    contents = file.read()

lines = [x for x in contents.split("\n")]
engine = []
for line in lines:
    engine.append([x for x in line])

def is_gear(engine, row_i, col_i):
    if row_i < 0 or row_i >= len(engine):
        return False
    if col_i < 0 or col_i >= len(engine[row_i]):
        return False
    element = engine[row_i][col_i]
    return element == "*"

class Position:
    def __init__(self, row_i, col_i):
        self.row_i = row_i
        self.col_i = col_i
    
    def __str__(self):
        return f"({self.row_i}, {self.col_i})"
    
    def __eq__(self, __value: object) -> bool:
        return self.row_i == __value.row_i and self.col_i == __value.col_i
    
    def __hash__(self) -> int:
        return hash((self.row_i, self.col_i))

class Gear:
    def __init__(self, position):
        self.adjacent_numbers = []
        self.position = position
    
    def add_adjacent_number(self, number):
        self.adjacent_numbers.append(number)
    
    def has_two_adjacent_numbers(self):
        return len(self.adjacent_numbers) == 2

    def multiply_all_adjacent_numbers(self):
        result = 1
        for number in self.adjacent_numbers:
            result *= number
        return result

gear_positions_dictionary = {}
working_number = []
neighbor_gears_positions = set()

for row_i in range(len(engine)):
    for col_i in range(len(engine[row_i])):
        element = engine[row_i][col_i]
        if element.isdigit():
            working_number.append(element)
            # looking for * neighbors of each number
            if is_gear(engine, row_i - 1, col_i - 1):
                neighbor_gears_positions.add(Position(row_i - 1, col_i - 1))
            if is_gear(engine, row_i - 1, col_i):
                neighbor_gears_positions.add(Position(row_i - 1, col_i))
            if is_gear(engine, row_i - 1, col_i + 1):
                neighbor_gears_positions.add(Position(row_i - 1, col_i + 1))
            if is_gear(engine, row_i, col_i - 1):
                neighbor_gears_positions.add(Position(row_i, col_i - 1))
            if is_gear(engine, row_i, col_i + 1):
                neighbor_gears_positions.add(Position(row_i, col_i + 1))
            if is_gear(engine, row_i + 1, col_i - 1):
                neighbor_gears_positions.add(Position(row_i + 1, col_i - 1))
            if is_gear(engine, row_i + 1, col_i):
                neighbor_gears_positions.add(Position(row_i + 1, col_i))
            if is_gear(engine, row_i + 1, col_i + 1):
                neighbor_gears_positions.add(Position(row_i + 1, col_i + 1))
        else:
            if len(working_number) > 0:
                for neighbor_gear_position in neighbor_gears_positions:
                    if str(neighbor_gear_position) not in gear_positions_dictionary:
                        gear_positions_dictionary[str(neighbor_gear_position)] = Gear(neighbor_gear_position)
                    gear_positions_dictionary[str(neighbor_gear_position)].add_adjacent_number(int("".join(working_number)))

            working_number = []
            neighbor_gears_positions = set()

sum = 0
for neighbor_gear_position in gear_positions_dictionary:
    if gear_positions_dictionary[str(neighbor_gear_position)].has_two_adjacent_numbers():
        sum += gear_positions_dictionary[str(neighbor_gear_position)].multiply_all_adjacent_numbers()

print(sum)
from pathlib import Path

path = Path(__file__).parent / "./input.txt"

with open(path, "r") as file:
    contents = file.read()

lines = [x for x in contents.split("\n")]
engine = []
for line in lines:
    engine.append([x for x in line])

def is_not_digit_or_dot(engine, row_i, col_i):
    if row_i < 0 or row_i >= len(engine):
        return False
    if col_i < 0 or col_i >= len(engine[row_i]):
        return False
    element = engine[row_i][col_i]

    if element == None:
        return False

    return not element.isdigit() and element != "."

numbers = []
working_number = []
is_adjacent_to_a_symbol = False

for row_i in range(len(engine)):
    for col_i in range(len(engine[row_i])):
        element = engine[row_i][col_i]
        if element.isdigit():
            working_number.append(element)
            if (
                is_not_digit_or_dot(engine,row_i-1,col_i-1) or 
                is_not_digit_or_dot(engine,row_i-1,col_i) or 
                is_not_digit_or_dot(engine,row_i-1,col_i+1) or 
                is_not_digit_or_dot(engine,row_i,col_i-1) or 
                is_not_digit_or_dot(engine,row_i,col_i+1) or 
                is_not_digit_or_dot(engine,row_i+1,col_i-1) or 
                is_not_digit_or_dot(engine,row_i+1,col_i) or 
                is_not_digit_or_dot(engine,row_i+1,col_i+1)
            ):
                is_adjacent_to_a_symbol = True
        else: # number is finished
            if is_adjacent_to_a_symbol:
                numbers.append(int("".join(working_number)))
            # and reset
            working_number = []
            is_adjacent_to_a_symbol = False

print(sum(numbers))
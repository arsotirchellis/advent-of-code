from pathlib import Path

path = Path(__file__).parent / "../input.txt"
with open(path, "r") as file:
    contents = file.read()
lines = [x for x in contents.split("\n")]
matrixes = []
current_matrix = []
for line in lines:
    line = line.strip()
    if line:
        current_matrix.append(list(line))
    else:
        if current_matrix:
            matrixes.append(current_matrix)
            current_matrix = []
if current_matrix:
    matrixes.append(current_matrix)


total_left_of_reflection_columns = 0
total_up_of_reflection_rows = 0

for matrix in enumerate(matrixes):

    # columns search
    max_col_reflection_index = 0
    col_len = len(matrix[0])
    for col_index in range(col_len-1):
        is_reflection = True
        elements_right = col_len - col_index - 1
        elements_left = col_index + 1
        min_len = min(elements_left, elements_right)
        for row_index in range(len(matrix)):
            for i in range(min_len):
                if matrix[row_index][col_index - i] != matrix[row_index][col_index+1+i]:
                    is_reflection = False
                    break
            if not is_reflection:
                break
        if is_reflection:
            max_col_reflection_index = col_index+1
    
    # rows search
    max_row_reflection_index = 0
    row_len = len(matrix)
    for row_index in range(row_len-1):
        is_reflection = True
        elements_up = row_index + 1
        elements_down = row_len - row_index - 1
        min_len = min(elements_up, elements_down)
        for col_index in range(len(matrix[0])):
            for i in range(min_len):
                if matrix[row_index - i][col_index] != matrix[row_index+1+i][col_index]:
                    is_reflection = False
                    break
            if not is_reflection:
                break
        if is_reflection:
            max_row_reflection_index = row_index+1

    total_left_of_reflection_columns += max_col_reflection_index
    total_up_of_reflection_rows += max_row_reflection_index

sum = total_left_of_reflection_columns + 100 * total_up_of_reflection_rows
print(sum)
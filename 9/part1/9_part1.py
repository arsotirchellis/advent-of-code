from pathlib import Path

path = Path(__file__).parent / "../input.txt"

with open(path, "r") as file:
    contents = file.read()

lines = [x for x in contents.split("\n")]

sequences = []

for i, line in enumerate(lines):
    sequences.append([int(num) for num in line.split(" ")])

extrapolations_sum = 0
for sequence in sequences:
    matrix = []
    matrix.append(sequence)
    i=0
    while True:
        matrix.append([])
    
        for j in range(len(matrix[i])-1):
            diff  = matrix[i][j+1] - matrix[i][j]
            matrix[i+1].append(diff)

        i+=1
        if set(matrix[i]) == {0}:
            break
    
    matrix[-1].append(0)
    for i in range(len(matrix)-2, -1, -1):
        sum = matrix[i+1][-1] + matrix[i][-1]
        matrix[i].append(sum)
        
    extrapolations_sum += matrix[0][-1]

print(extrapolations_sum)
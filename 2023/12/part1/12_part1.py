from pathlib import Path

path = Path(__file__).parent / "../input.txt"
with open(path, "r") as file:
    contents = file.read()
lines = [x for x in contents.split("\n")]

records = []
for i, line in enumerate(lines):
    records.append([[],[]])
    records[i][0] = [x for x in line.split(" ")[0]]
    records[i][1] = [int(x) for x in line.split(" ")[1].split(",")]

def matches(springs, numbers, origin):
    springs = springs.copy()
    numbers = numbers.copy()
    result = 0

    if numbers[0] == 0:
        numbers.pop(0)

        if len(numbers) != 0:
            origin = numbers[0]

        # group is finished but we still have springs left. So its not a valid combination
        if len(springs) != 0 and springs[0] == "#":
            return 0

        # if a group is just finished, we cant have a spring after it. Its a dot.
        if len(springs) != 0:
            springs.pop(0)

    # removing the . at the start of the springs
    while len(springs) != 0 and springs[0] == ".":
        if len(numbers) > 0 and numbers[0] != origin: # found a dot while expecting a spring
            return 0

        springs.pop(0)

    if len(springs) == 0:
        if len(numbers) == 0:
            return 1
        else:
            return 0

    if len(numbers) == 0:
        if springs.count("#") == 0:
            return 1
        else:
            return 0

    if springs[0] == "#": # forced to have a spring, so remove it from the first number
        if len(numbers) == 0:
            return 0 # if there are no numbers left, we cant have a spring, so its a dead end
    
        numbers[0] = numbers[0]-1
        springs.pop(0)
        result = matches(springs, numbers, origin)
    elif springs[0] == "?":
        if len(numbers) == 0:
            return 0 # if there are no numbers left, we cant have a spring, so its a dead end

        numbers[0] = numbers[0] - 1 
        result += matches(springs[1:], numbers, origin)

        if (numbers[0] + 1) == origin:
            numbers[0] = numbers[0] + 1
            result += matches(springs[1:], numbers, origin)
    
    return result

sum = 0
for record in records:
    sum += matches(record[0], record[1], record[1][0])
print(sum)
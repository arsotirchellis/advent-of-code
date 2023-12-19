from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, "r") as file:
    contents = file.read()
steps = [x for x in contents.split(",")]

sum = 0
for step in steps:
    current_value = 0
    for char in step:
        # ascii value
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    sum += current_value

print(sum)

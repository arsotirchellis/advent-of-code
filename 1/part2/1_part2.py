from pathlib import Path

path = Path(__file__).parent / "./input.txt"

with open(path, "r") as file:
    contents = file.read()

calibrations = [x for x in contents.split("\n")]
print(calibrations)

numbers = []
for calibration in calibrations:
    characters = [x for x in calibration]
    number = 0
    for c in characters:
        if c.isdigit():
            number = 10 * int(c)
            break 
    for c in reversed(characters):
        if c.isdigit():
            number += int(c)
            break
    numbers.append(number)
    
print(sum(numbers))

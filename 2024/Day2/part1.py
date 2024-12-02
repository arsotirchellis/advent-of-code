from pathlib import Path

path = Path(__file__).parent / "test.txt"
with open(path, "r") as file:
    contents = file.read()
lines = [x for x in contents.split("\n")]

reports = [[int(num) for num in x.split(" ") if num] for x in lines if x]

def is_safe(report):
    min_level_increase = 1
    max_level_increase = 3

    increasing = True
    decreasing = True

    for i in range(1, len(report)):
        if increasing:
            if (report[i] - report[i - 1] < min_level_increase) or (report[i] - report[i - 1] > max_level_increase):
                increasing = False
        if decreasing:
            if (report[i] - report[i - 1] < max_level_increase * -1) or (report[i] - report[i - 1] > min_level_increase * -1):
                decreasing = False

        if not increasing and not decreasing:
            break

    return increasing or decreasing



valid_reports = 0
for report in reports:
    if is_safe(report):
        valid_reports += 1

print(valid_reports)
from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, "r") as file:
    contents = file.read()
lines = [x for x in contents.split("\n")]

reports = [[int(num) for num in x.split(" ") if num] for x in lines if x]

def is_safe(report, recursive=False):
    min_level_increase = 1
    max_level_increase = 3

    increasing = True
    decreasing = True

    increasing_problematic_index = -1
    decreasing_problematic_index = -1

    for i in range(1, len(report)):
        if increasing:
            if (report[i] - report[i - 1] < min_level_increase) or (report[i] - report[i - 1] > max_level_increase):
                increasing = False
                increasing_problematic_index = i
        if decreasing:
            if (report[i] - report[i - 1] < max_level_increase * -1) or (report[i] - report[i - 1] > min_level_increase * -1):
                decreasing = False
                decreasing_problematic_index = i
        if not increasing and not decreasing:
            break

    if not increasing and not decreasing:
        if recursive:
            report_without_increasing_problematic_element = report[:increasing_problematic_index] + report[increasing_problematic_index + 1:]
            report_without_decreasing_problematic_element = report[:decreasing_problematic_index] + report[decreasing_problematic_index + 1:]
            report_without_first_element = report[1:]
            report_without_last_element = report[:-1]
            second_chance = is_safe(report_without_increasing_problematic_element) or is_safe(report_without_decreasing_problematic_element) or is_safe(report_without_first_element) or is_safe(report_without_last_element)
            return second_chance
        else:
            return False
    else:
        return True



valid_reports = 0
for report in reports:
    if is_safe(report, recursive=True):

        valid_reports += 1

print(valid_reports)

from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, "r") as file:
    contents = file.read()
lines = [x for x in contents.split("\n")]

left_list = []
right_list = []
for line in lines:
    left, right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))


left_list = sorted(left_list)
right_list = sorted(right_list)

dist_sum = 0
for i in range(len(left_list)):
    dist_sum += abs(left_list[i] - right_list[i])

print(dist_sum)

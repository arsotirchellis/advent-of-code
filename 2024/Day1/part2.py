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

# dict: key=number value:number of occurences
right_list_occurences_dict = {}
for number in right_list:
    if number not in right_list_occurences_dict:
        right_list_occurences_dict[number] = 1
    else:
        right_list_occurences_dict[number] += 1

dist_sum = 0
for number in left_list:
    if number in right_list_occurences_dict:
        dist_sum += number*right_list_occurences_dict[number]

print(dist_sum)

from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, "r") as file:
    contents = file.read()
steps = [x for x in contents.split(",")]

def hash_algo(str):
    current_value = 0
    for char in str:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length
    def __hash__(self):
        return hash_algo(self.label)
    def __eq__(self, other):
        return self.label == other.label

class Box:
    def __init__(self):
        self.lenses = []
    def replace_or_add_lens(self, lens):
        try:
            lens_index = self.lenses.index(lens)
        except ValueError:
            lens_index = -1

        if lens_index == -1:
            self.lenses.append(lens)
        else:
            self.lenses[lens_index] = lens
    def remove_lens(self, lens):
        try:
            lens_index = self.lenses.index(lens)
        except ValueError:
            lens_index = -1

        if lens_index != -1:
            del self.lenses[lens_index]

boxes = [Box() for i in range(256)]

for step in steps:
    label = ""
    focal_length = 0
    if step.endswith("-"):
        label = step[:-1]
        relevant_box = boxes[hash_algo(label)]
        relevant_box.remove_lens(Lens(label, 0))
    else:
        label = step[:-2]
        focal_length = int(step[-1])
        relevant_box = boxes[hash_algo(label)]
        relevant_box.replace_or_add_lens(Lens(label, focal_length))

sum = 0
for i, box in enumerate(boxes):
    for j, len in enumerate(box.lenses):
        power = (i + 1) * (j + 1) * len.focal_length
        sum += power
print(sum)
from pathlib import Path

path = Path(__file__).parent / "../input.txt"

with open(path, "r") as file:
    contents = file.read()

lines = [x for x in contents.split("\n")]

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
    
    def go_left(self):
        return self.left
    
    def go_right(self):
        return self.right
    
    def name_ends_with(self, string):
        return self.name.endswith(string)

instructions = lines[0]
nodes_dict = {}
working_nodes = []
for i in range(2, len(lines)):
    name = lines[i].split("=")[0].strip()
    left_name = lines[i].split("=")[1].split(",")[0].strip()[1:]
    right_name = lines[i].split("=")[1].split(",")[1].strip()[0:-1]

    left_node = Node(left_name, None, None)
    if left_name not in nodes_dict:
        nodes_dict[left_name] = left_node
    else:
        left_node = nodes_dict[left_name]

    right_node = Node(right_name, None, None)
    if right_name not in nodes_dict:
        nodes_dict[right_name] = right_node
    else:
        right_node = nodes_dict[right_name]

    if name not in nodes_dict:
        current_node = Node(name, left_node, right_node)
        nodes_dict[name] = current_node
    else:
        current_node = nodes_dict[name]
        current_node.left = left_node
        current_node.right = right_node

    if current_node.name_ends_with("A"):
        working_nodes.append(current_node)


instructions_index = 0
working_nodes_min_steps = []

for node in working_nodes:
    steps_count = 0
    while True:
    # circle again and again the instructions
        if instructions_index >= len(instructions):
            instructions_index = 0
        instruction = instructions[instructions_index]
        instructions_index += 1
        steps_count += 1
        if instruction == "L":
            node = node.go_left()
        else:
            node = node.go_right()
        
        if node.name_ends_with("Z"):
            working_nodes_min_steps.append(steps_count)
            break

import math

lcm_value = working_nodes_min_steps[0]
for i in working_nodes_min_steps[1:]:
    lcm_value = math.lcm(lcm_value, i)

print(lcm_value)

from pathlib import Path

path = Path(__file__).parent / "test.txt"
with open(path, "r") as file:
    contents = file.read()
lines = [x for x in contents.split("\n")]

matrix = []
for line in lines:
    line = line.strip()
    if line:
        matrix.append(list(line))

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
    def from_direction(self):
        if self.parent is None:
            return 'L' # for the start node :D
        if self.parent.position[1] < self.position[1]:
            return 'L'
        if self.parent.position[1] > self.position[1]:
            return 'R'
        if self.parent.position[0] < self.position[0]:
            return 'U'
        if self.parent.position[0] > self.position[0]:
            return 'D'
    def __eq__(self, other):
        return self.position == other.position
    def __hash__(self):
        return hash(self.position)
    
def heuristic(node, goal):
    return abs(node.position[0] - goal.position[0]) + abs(node.position[1] - goal.position[1])

start_node = Node(None, (0, 0))
start_node.g = start_node.h = start_node.f = 0
end_node = Node(None, (len(matrix)-1, len(matrix[0])-1))
end_node.g = end_node.h = end_node.f = 0

to_explore = []
explored = set()

path = []

to_explore.append(start_node)

# create a copy of the matrix
painted_matrix = [x[:] for x in matrix]


while len(to_explore) > 0:
    current_node = to_explore.pop(0)
    painted_matrix[current_node.position[0]][current_node.position[1]] = '.'
    explored.add(current_node)

    if current_node == end_node:
        current = current_node
        while current is not None:
            path.append(current.position)
            current = current.parent
        break

    children = []
    
    for new_position in [(0, -1, 'R'), (0, 1, 'L'), (-1, 0, 'D'), (1, 0, 'U')]:
        new_node_from_direction = new_position[2]
        new_node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
        if (
            new_node_position[0] > (len(matrix) - 1) or
            new_node_position[0] < 0 or
            new_node_position[1] > (len(matrix[0]) -1) or
            new_node_position[1] < 0
        ):
            continue

        # we can't turn 180 degrees
        if current_node.from_direction() == 'L' and new_node_from_direction == 'R':
            continue
        if current_node.from_direction() == 'R' and new_node_from_direction == 'L':
            continue
        if current_node.from_direction() == 'U' and new_node_from_direction == 'D':
            continue
        if current_node.from_direction() == 'D' and new_node_from_direction == 'U':
            continue

        if ( # go 3 straight to the same direction, skip
            current_node.from_direction() == new_node_from_direction and
            current_node.parent is not None and 
            current_node.parent.from_direction() == new_node_from_direction and 
            current_node.parent.parent is not None and 
            current_node.parent.parent.from_direction() == new_node_from_direction
        ):
            continue
        
        new_node = Node(parent=current_node, position=(new_node_position[0], new_node_position[1]))
        children.append(new_node)

    for child in children:
        if child in explored:
            continue

        child.g = child.parent.g + int(matrix[child.position[0]][child.position[1]])
        child.h = heuristic(child, end_node)
        child.f = child.g + child.h

        if child in to_explore:
            index = to_explore.index(child)
            if to_explore[index].g > child.g:
                to_explore[index] = child
            else:
                continue

        to_explore.append(child)

    to_explore.sort(key=lambda x: x.f)

sum = 0
# based on path paint the matrix
for p in path:
    sum += int(matrix[p[0]][p[1]])
    matrix[p[0]][p[1]] = '.'
print(sum)
from pathlib import Path

path = Path(__file__).parent / "./input.txt"

with open(path, "r") as file:
    contents = file.read()

lines = [x for x in contents.split("\n")]
seeds_line = lines[0]
seeds_parts = seeds_line.split(": ")

class Group:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __contains__(self, item):
        return self.start <= item <= self.end
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Group):
            return False
        return self.start == __value.start and self.end == __value.end
    
    def __eq__(self, other):
        if isinstance(other, Group):
            return (self.start, self.end) == (other.start, other.end)
        return False
    
    def __hash__(self) -> int:
        return hash((self.start, self.end))
    
    def has_intersection_with_range(self, other_start, other_end):
        return ((self.start >= other_start and self.start <= other_end )
                or 
                (other_start >= self.start and other_start <= self.end))
    
    def map_intersection(self, source_start, source_end, destination_start, destination_end):
        if self.has_intersection_with_range(source_start, source_end):
            self.start = destination_start + self.start - source_start
            self.end = destination_end - (source_end - self.end)

    def split_group_based_on_intersection(self, other_start, other_end) -> list:
        if self.has_intersection_with_range(other_start, other_end):
            # intersection on the left
            if other_start <= self.start and other_end <= self.end:
                return [Group(self.start, other_end), Group(other_end+1, self.end)]
            # intersection on the right
            elif other_start > self.start and other_end > self.end:
                return [Group(self.start, other_start-1), Group(other_start, self.end)]
            # intersection is the whole group
            elif other_start <= self.start and other_end >= self.end:
                return [Group(self.start, self.end)]
            # intersection in the middle
            else:
                return [Group(self.start, other_start-1), Group(other_start, other_end), Group(other_end+1, self.end)]
        else:
            return [self]
        
    def map_to_new_values(self, new_start, new_end):
        self.start = new_start
        self.end = new_end

seed_ranges = [int(seed) for seed in seeds_parts[1].split(" ")]
seed_pairs = list(zip(seed_ranges[::2], seed_ranges[1::2]))

groups = set()
for seed_pair in seed_pairs:
    groups.add(Group(seed_pair[0], seed_pair[0] + seed_pair[1] - 1))
groups_mapped = set()

for line in lines[1:]:
    if len(line) == 0:
        groups_mapped = set()
        continue
    if not line[0].isdigit():
        continue
    else:
        maps = line.split(" ")
        destination_range_start = int(maps[0])
        source_range_start = int(maps[1])
        range = int(maps[2])

        groups_to_add = []
        groups_to_remove = []
        for group in groups:
            if (group.start, group.end) in groups_mapped:
                continue

            if group.has_intersection_with_range(source_range_start, source_range_start + range - 1):
                spliced_groups = group.split_group_based_on_intersection(source_range_start, source_range_start + range - 1)
                for group_to_add in spliced_groups:
                    if group_to_add.has_intersection_with_range(source_range_start, source_range_start + range - 1):
                        group_to_add.map_intersection(source_range_start, source_range_start + range - 1, destination_range_start, destination_range_start + range - 1)
                        groups_mapped.add((group_to_add.start, group_to_add.end))
                groups_to_add.extend(spliced_groups)
                groups_to_remove.append(group)
        for group in groups_to_remove:
            groups.remove(group)
        groups.update(groups_to_add)
        
sorted_groups = sorted(groups, key=lambda group: group.start)
print(sorted_groups)

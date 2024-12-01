from pathlib import Path

path = Path(__file__).parent / "./input.txt"

with open(path, "r") as file:
    contents = file.read()

lines = [x for x in contents.split("\n")]
seeds_line = lines[0]
seeds_parts = seeds_line.split(": ")

seeds = [int(seed) for seed in seeds_parts[1].split(" ")]

indexes_mapped = set()

for line in lines[1:]:
    if len(line) == 0 or not line[0].isdigit():
        indexes_mapped = set()
        continue
    else:
        maps = line.split(" ")
        destination_range_start = int(maps[0])
        source_range_start = int(maps[1])
        range = int(maps[2])
        
        for i, seed in enumerate(seeds):
            if i in indexes_mapped:
                continue

            if (seeds[i] >= source_range_start) and (seeds[i] < source_range_start + range):
                seeds[i] = destination_range_start + (seeds[i] - source_range_start)
                indexes_mapped.add(i)

print(sorted(seeds))
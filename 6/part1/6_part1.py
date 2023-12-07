from pathlib import Path

path = Path(__file__).parent / "./input.txt"

with open(path, "r") as file:
    contents = file.read()

lines = [x for x in contents.split("\n")]

times = list(map(int, filter(None, lines[0].split(":")[1].strip().split(" "))))
distances = list(map(int, filter(None, lines[1].split(":")[1].strip().split(" "))))
races = list(zip(times, distances))

solution = 1
for race in races:
    beat_record_count = 0
    race_ms = race[0]
    race_distance_record = race[1]
    for throttle_ms in range(race_ms):
        run_ms = race_ms - throttle_ms
        if run_ms * throttle_ms > race_distance_record:
            beat_record_count += 1

    solution *= beat_record_count

print(solution)
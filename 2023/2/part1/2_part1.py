from pathlib import Path

path = Path(__file__).parent / "./input.txt"

with open(path, "r") as file:
    contents = file.read()

game_strings = [x for x in contents.split("\n")]

# Game 12: 8 blue, 7 green; 2 green, 2 red, 7 blue; 4 green, 1 red, 20 blue; 5 green, 13 blue, 2 red

dict = {}

for game in game_strings:
    game_part = game.split(":")[0].strip()
    game_id = game_part.split(" ")[1].strip()

    dict[game_id] = []

    options_part = game.split(":")[1].strip()
    options = options_part.split(";")
    for option in options:
        red = 0
        green = 0
        blue = 0
        option_parts = option.strip().split(", ")
        for option_part in option_parts:
            if "red" in option_part:
                red = option_part.split(" ")[0].strip()
            elif "green" in option_part:
                green = option_part.split(" ")[0].strip()
            elif "blue" in option_part:
                blue = option_part.split(" ")[0].strip()

        dict[game_id].append({
            "red" : red,
            "green" : green,
            "blue" : blue
        })

print(dict)

game_ids = [] 
for game_id, options in dict.items():
    valid_game = True
    for option in options:
        if int(option["red"]) > 12 or int(option["green"]) > 13 or int(option["blue"]) > 14:
            valid_game = False
            break
    if valid_game:
        game_ids.append(int(game_id))

print(sum(game_ids))
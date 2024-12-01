#!/bin/sh

YEAR=$(date +%Y)
YEAR_FOLDER="$YEAR"

if [ ! -d "$YEAR_FOLDER" ]; then
    mkdir "$YEAR_FOLDER"
    for i in $(seq 1 25); do
        DAY_FOLDER="$YEAR_FOLDER/Day$i"
        mkdir -p "$DAY_FOLDER"
        
        touch "$DAY_FOLDER/input.txt"
        touch "$DAY_FOLDER/test.txt"
        touch "$DAY_FOLDER/notes.md"
        
        for PART in part1.py part2.py; do
            cat << 'EOF' > "$DAY_FOLDER/$PART"
from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, "r") as file:
    contents = file.read()
lines = [x for x in contents.split("\n")]

print("Good luck !")
EOF
        done
    done
    echo "Folder '$YEAR_FOLDER' and subfolders created successfully."
else
    echo "Folder '$YEAR_FOLDER' already exists. No action taken."
fi
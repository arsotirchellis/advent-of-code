from pathlib import Path

def recursive_trie_construction(dictionary, characters, value) -> dict:    
    # the goal is to create a trie that looks like this:
    # trie = {
    #     "o" : {
    #         "n" : {
    #             "e" : 1
    #         }
    #     },
    #     "t" : {
    #         "w" : {
    #             "o" : 2
    #         },
    #         "h" : {
    #             "r" : {
    #                 "e" : {
    #                     "e" : 3
    #                 }
    #             }
    #         },
    #     }
    # }
    first_letter = characters[0]
    rest_of_characters = characters[1:]
    if first_letter not in dictionary:
        dictionary[first_letter] = {}

    if len(rest_of_characters) == 0:
        dictionary[first_letter] = value
        return dictionary

    dictionary[first_letter] = recursive_trie_construction(dictionary[first_letter], rest_of_characters, value)
    return dictionary
    
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

numbers_trie = {}
for index, number in enumerate(numbers):
    numbers_trie = recursive_trie_construction(numbers_trie, number, index + 1)

path = Path(__file__).parent / "./input.txt"
with open(path, "r") as file:
    contents = file.read()

calibrations = [x for x in contents.split("\n")]

numbers = []
for calibration in calibrations:
    characters = [x for x in calibration]
    calibration_numbers = []
    
    working_trie = numbers_trie
    working_tries = []
    indexes_to_delete = []

    for c in characters:
        if c.isdigit():
            calibration_numbers.append(int(c))
            working_tries = []
            continue

        for i, working_trie in enumerate(working_tries):
            if c in working_trie:
                working_tries[i] = working_trie[c]
                if type(working_tries[i]) == int:
                    calibration_numbers.append(working_tries[i])
                    working_tries = []
                    break
            else:
                indexes_to_delete.append(i)
        
        if len(indexes_to_delete) > 0:
            new_working_tries = []
            for i, working_trie in enumerate(working_tries):
                if i not in indexes_to_delete:
                    new_working_tries.append(working_trie)
            working_tries = new_working_tries
            indexes_to_delete = []

        if c in numbers_trie:
            working_tries.append(numbers_trie[c])
            
    number = 0
    number += 10 * calibration_numbers[0]
    number += calibration_numbers[-1]

    numbers.append(number)

print(sum(numbers))

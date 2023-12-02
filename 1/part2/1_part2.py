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
reverted_numbers = [x[::-1] for x in numbers]

numbers_trie = {}
for index, number in enumerate(numbers):
    numbers_trie = recursive_trie_construction(numbers_trie, number, index + 1)

reverted_numbers_trie = {}
for index, number in enumerate(reverted_numbers):
    reverted_numbers_trie = recursive_trie_construction(reverted_numbers_trie, number, index + 1)

path = Path(__file__).parent / "./input.txt"
with open(path, "r") as file:
    contents = file.read()

calibrations = [x for x in contents.split("\n")]
calibrations = [
'sevene'
]
# one
# two
# three
# four
# five
# six
# seven
# eight
# nine


numbers = []
for calibration in calibrations:
    characters = [x for x in calibration]
    calibration_numbers = []
    number = 0
    
    working_trie = numbers_trie
    for c in characters:
        if c.isdigit():
            number = 10 * int(c)
            break
        if c in working_trie:
            working_trie = working_trie[c]
            if type(working_trie) == int:
                number = 10 * int(working_trie)
                break
        elif c in numbers_trie:
            working_trie = numbers_trie[c]
            if type(working_trie) == int:
                number = 10 * int(working_trie)
                break
        else:
            working_trie = numbers_trie
            
    working_trie = reverted_numbers_trie
    for c in reversed(characters):
        if c.isdigit():
            number += int(c)
            break
        if c in working_trie:
            working_trie = working_trie[c]
            if type(working_trie) == int:
                number += int(working_trie)
                break
        elif c in reverted_numbers_trie:
            working_trie = reverted_numbers_trie[c]
            if type(working_trie) == int:
                number += int(working_trie)
                break
        else:
            working_trie = reverted_numbers_trie
            continue

    numbers.append(number)

print(sum(numbers))

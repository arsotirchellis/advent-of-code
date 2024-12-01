from pathlib import Path

path = Path(__file__).parent / "./input.txt"

with open(path, "r") as file:
    contents = file.read()

cards_lines = [x for x in contents.split("\n")]

class Card:
    def __init__(self, name, winning_numbers, actual_numbers) -> None:
        self.name = name
        self.winning_numbers = sorted(winning_numbers)
        self.actual_numbers = sorted(actual_numbers)
    
    def get_name(self):
        return self.name

    def common_numbers(self):
        common_numbers = []
        winning_numbers_pointer = 0
        actual_numbers_pointer = 0
        
        while winning_numbers_pointer < len(self.winning_numbers) and actual_numbers_pointer < len(self.actual_numbers):
            if self.actual_numbers[actual_numbers_pointer] == self.winning_numbers[winning_numbers_pointer]:
                common_numbers.append(self.actual_numbers[actual_numbers_pointer])
                winning_numbers_pointer += 1
                actual_numbers_pointer += 1
            elif self.actual_numbers[actual_numbers_pointer] < self.winning_numbers[winning_numbers_pointer]:
                actual_numbers_pointer += 1
            elif self.actual_numbers[actual_numbers_pointer] > self.winning_numbers[winning_numbers_pointer]:
                winning_numbers_pointer += 1
        
        return common_numbers
    
    def common_numbers_len(self):
        return len(self.common_numbers())

cards = {}
cards_quantity = {}
for card in cards_lines:
    name = card.split(":")[0]
    name = name.split(" ")[-1]

    numbers = card.split(":")[1]
    winning_numbers = []
    for number in numbers.split("|")[0].split(" "):
        if number != ' ' and number != '':
            winning_numbers.append(int(number))
    
    actual_numbers = []
    for number in numbers.split("|")[1].split(" "):
        if number != ' ' and number != '':
            actual_numbers.append(int(number))
    
    cards[name] = Card(name, winning_numbers, actual_numbers)
    cards_quantity[name] = 1


for i in range(len(cards)):
    card_index = i+1
    card = cards[str(card_index)]
    multiplier_of_card = cards_quantity[str(card_index)]
    print()
    print()
    for next_card_index in range(card_index, card_index + card.common_numbers_len()):
        next_card_index +=1
        if next_card_index < (len(cards)+1):
            cards_quantity[str(next_card_index)] += 1 * multiplier_of_card

total_cards_quantity = 0
for card_quantity in cards_quantity.values():
    total_cards_quantity += card_quantity
print(total_cards_quantity)
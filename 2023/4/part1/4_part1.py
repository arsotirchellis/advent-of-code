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
    
    def points_won(self):
        common_numbers = self.common_numbers()
        if len(common_numbers) > 0:
            return 2**(len(common_numbers)-1)
            
        else:
            return 0
    def __str__(self) -> str:
        return f"{self.name}: {self.common_numbers()}: points won: {self.points_won()}"

cards = []
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
    
    cards.append(Card(name, winning_numbers, actual_numbers))

sum = 0
for card in cards:
    sum += card.points_won()
print(sum)

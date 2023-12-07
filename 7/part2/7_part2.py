from pathlib import Path

path = Path(__file__).parent / "../input.txt"

with open(path, "r") as file:
    contents = file.read()

lines = [x for x in contents.split("\n")]


class Hand:
    def __init__(self, cards_str: str, bid: int):
        self.bid = int(bid)

        self.cards = []
        for card in cards_str:
            if card == "A":
                self.cards.append(14)
            elif card == "K":
                self.cards.append(13)
            elif card == "Q":
                self.cards.append(12)
            elif card == "J":
                self.cards.append(1)  # <------------- value is less that 2 now
            elif card == "T":
                self.cards.append(10)
            else:
                self.cards.append(int(card))

        self.cards_dict_counts = {}
        for card in self.cards:
            if card not in self.cards_dict_counts:
                self.cards_dict_counts[card] = 1
            else:
                self.cards_dict_counts[card] += 1

    def __lt__(self, other):
        # joker counts, by default are zero
        self_joker_count = self.cards_dict_counts.get(1, 0)
        other_joker_count = other.cards_dict_counts.get(1, 0)

        self_cards_dict_counts_without_jokers = self.cards_dict_counts.copy()
        self_cards_dict_counts_without_jokers.pop(1, None)

        other_cards_dict_counts_without_jokers = other.cards_dict_counts.copy()
        other_cards_dict_counts_without_jokers.pop(1, None)

        self_dict_values = sorted(
            self_cards_dict_counts_without_jokers.values())

        other_dict_values = sorted(
            other_cards_dict_counts_without_jokers.values())

        self_highest_value = max(
            self_dict_values) if self_dict_values else 0
        other_highest_value = max(
            other_dict_values) if other_dict_values else 0

        self_highest_value = self_highest_value + self_joker_count
        other_highest_value = other_highest_value + other_joker_count

        if (self_highest_value) < (other_highest_value):
            return True
        if (self_highest_value) > (other_highest_value):
            return False

        # check for full house
        if len(other_cards_dict_counts_without_jokers) == 2 and len(self_cards_dict_counts_without_jokers) > 2:
            return True
        if len(self_cards_dict_counts_without_jokers) == 2 and len(other_cards_dict_counts_without_jokers) > 2:
            return False

        if (len(other.cards_dict_counts) == 3 and other_highest_value == 2) and len(self.cards_dict_counts) > 3:
            return True
        if (len(self.cards_dict_counts) == 3 and self_highest_value == 2) and len(other.cards_dict_counts) > 3:
            return False

        # check card by card
        for i in range(5):
            if self.cards[i] < other.cards[i]:
                return True
            elif self.cards[i] > other.cards[i]:
                return False

        return False

    def __eq__(self, other):
        return self.cards == other.cards


hands = []
for line in lines:
    line_parts = line.split(" ")
    hands.append(Hand(cards_str=line_parts[0], bid=line_parts[1]))

sorted_hands = sorted(hands)

response_sum = 0
for i, hand in enumerate(sorted_hands):
    i += 1
    response_sum += i * hand.bid
print(response_sum)

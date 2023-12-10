# Open the file and read all lines
with open("hands.txt", "r") as file:
    lines = file.readlines()

import functools

hand_ranks = {
    "High Card": 1,
    "One Pair": 2,
    "Two Pair": 3,
    "Three of a Kind": 4,
    "Full House": 5,
    "Four of a Kind": 6,
    "Five of a Kind": 7,
}

type_dict = {}  # store the type of cards
for line in lines:
    line = line.strip().split(" ")
    line[1] = int(line[1])
    # Example of line[0] = "KK677"
    char_count = {}
    for char in line[0]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # check if any character count is 4
    if any(value == 5 for value in char_count.values()):
        type_dict[line[0]] = [line[1], "Five of a Kind"]
    elif any(value == 4 for value in char_count.values()):
        type_dict[line[0]] = [line[1], "Four of a Kind"]
    elif any(value == 3 for value in char_count.values()) and any(
        value == 2 for value in char_count.values()
    ):
        type_dict[line[0]] = [line[1], "Full House"]
    elif any(value == 3 for value in char_count.values()):
        type_dict[line[0]] = [line[1], "Three of a Kind"]
    elif list(char_count.values()).count(2) == 2:
        type_dict[line[0]] = [line[1], "Two Pair"]
    elif list(char_count.values()).count(2) == 1:
        type_dict[line[0]] = [line[1], "One Pair"]
    else:
        type_dict[line[0]] = [line[1], "High Card"]


# "Five of a Kind" > "Four of a Kind" > "Full House" > "Three of a Kind" > "Two Pair" > "One Pair" > "High Card"
# Sort the hands by their hand_ranks
def sort_by_hand_ranks(type_dict):
    sorted_hands = sorted(
        type_dict.items(), key=lambda x: (hand_ranks[x[1][1]], x[1][0]), reverse=True
    )
    return sorted_hands


# If two or more type of hands are the same then sort the value of the card.
# Check first card value of those two or more cards, if same then check second card values, and so on.
def card_value(card):
    """Assigns a numerical value to a card for sorting purposes."""
    card_order = "23456789TJQKA"
    return card_order.index(card)

def sort_by_card_values(sorted_hands):
    def compare_hands(hand1, hand2):
        # If the type of hands are different, keep the current order.
        if hand1[1][1] != hand2[1][1]:
            return 0

        # Sort the cards in each hand by their value
        hand1_values = [card_value(card) for card in hand1[0]]
        hand2_values = [card_value(card) for card in hand2[0]]

        # Compare the card values of the two hands
        for card1, card2 in zip(hand1_values, hand2_values):
            if card1 > card2:
                return -1
            elif card1 < card2:
                return 1
        return 0

    return sorted(sorted_hands, key=functools.cmp_to_key(compare_hands))

# Update your existing code to use this function
sorted_hands = sort_by_hand_ranks(type_dict)
sorted_hands = sort_by_card_values(sorted_hands)

for hand in sorted_hands:
    print(f"Hand: {hand[0]}, Value: {hand[1][0]}, Type: {hand[1][1]}")

# reverse the list
sorted_hands.reverse()

sum_total = 0
for hand in range(0, len(sorted_hands), 1):
    sum_total += ((hand + 1) * sorted_hands[hand][1][0])

print("Total Winnings: ", sum_total)

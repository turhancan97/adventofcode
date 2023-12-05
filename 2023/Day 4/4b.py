with open("scratchcards.txt", "r", encoding="utf-8") as f:  # Open the file
    lines = f.readlines()  # Read the lines

win_dict = {}  # Create a dictionary for the winners
for line in lines:  # For each line
    seperation = line.split(":")
    # Find the card number
    card_id = int(seperation[0][4:])
    # Find the line
    line = seperation[1].strip()
    # Seperate the line with |
    line = line.split("|")
    # Turn into a interger of each element in the list
    line[0] = line[0].strip().replace("  ", " ").split(" ")
    line[1] = line[1].strip().replace("  ", " ").split(" ")
    # Turn into a interger of each element in the list
    line[0] = [int(i) for i in line[0]]
    line[1] = [int(i) for i in line[1]]
    # Find the numbers that are the same in both lists
    same = set(line[0]).intersection(line[1])
    win_number = len(same)
    # Add to the dictionary
    win_dict[card_id] = win_number
# set a dictory that has same key values of win_dict but all values are 0
win_new_dict = {key: 1 for key in win_dict}
for key, value in win_dict.items():  # For each item in the dictionary
    for _ in range(win_new_dict[key]):
        for i in range(1, value + 1):
            win_new_dict[key + i] += 1

# Sum all the values in the dictionary
total = sum(win_new_dict.values())
print("Total number of winning cards:", total)

with open("scratchcards.txt", "r", encoding="utf-8") as f:  # Open the file
    lines = f.readlines()  # Read the lines

store_point = []  # list to store the points
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
    # Print the card number and the numbers that are the same
    print(f"Card {card_id}: {same}")
    # if same 0 no points, if same 1 1 point, if same 2 2 points, if same 3 4 points, if same 4 8 points
    if len(same) == 0:
        store_point.append(0)
    else:
        store_point.append(2 ** (len(same) - 1))

# Print the total points
print(f"Total points: {sum(store_point)}")

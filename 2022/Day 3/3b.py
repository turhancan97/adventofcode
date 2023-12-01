# Initialize the sum of priorities to 0
sum_of_priorities = 0

with open('rucksacks.txt', 'r', encoding="utf-8") as f: # Open the file
    rucksacks = f.readlines() # Read the lines
    rucksacks = [rucksack.strip() for rucksack in rucksacks] # Strip the lines
    
    # Split the list of rucksacks into groups of three
    for i in range(0, len(rucksacks), 3):
        group = rucksacks[i:i+3]
        
        # Create a dictionary that maps each character to the number of times
        # it appears in all three rucksacks
        for rucksack1 in group[0]:
            if rucksack1 in group[1] and rucksack1 in group[2]:
                if rucksack1.islower():
                    sum_of_priorities += ord(rucksack1) - 96
                else:
                    sum_of_priorities += ord(rucksack1) - 38
                break

# Print the sum of priorities
print(sum_of_priorities)
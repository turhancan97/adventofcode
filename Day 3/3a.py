# Initialize the sum of priorities to 0
sum_of_priorities = 0

with open('rucksacks.txt', 'r', encoding="utf-8") as f: # Open the file
    rucksacks = f.readlines() # Read the lines

    # Loop through each rucksack
    for rucksack in rucksacks:
        # Split the rucksack into two compartments
        comp1, comp2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

        # Create dictionaries that map each character to the number of times
        # it appears in each compartment
        counts1, counts2 = {}, {}
        for ch in comp1:
            counts1[ch] = counts1.get(ch, 0) + 1
        for ch in comp2:
            counts2[ch] = counts2.get(ch, 0) + 1

        # Loop through the keys in the first dictionary
        for ch in counts1.keys():
            # If the character appears in both compartments, add its priority
            # to the sum of priorities
            if ch in counts2:
                # Lowercase item types a through z have priorities 1 through 26.
                # Uppercase item types A through Z have priorities 27 through 52.
                if ch.islower():
                    sum_of_priorities += ord(ch) - 96
                else:
                    sum_of_priorities += ord(ch) - 38

    # Print the sum of priorities
    print(sum_of_priorities)
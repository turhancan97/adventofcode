pairs = 0 # number of pairs that do the ranges overlap
with open('assignment.txt', 'r', encoding="utf-8") as f: # Open the file
    assignment = f.readlines() # Read the lines of the file
    assignment = [line.strip() for line in assignment] # Remove the newline character from each line

    for line in assignment:
        # delete the '-' and ',' and split the line into two parts
        line = line.replace('-', ' ').replace(',', ' ').split()
        # convert the strings to integers
        line = [int(i) for i in line]
        if not (line[1] < line[2] or line[3] < line[0]): # if the ranges overlap
            pairs += 1

    print(pairs)
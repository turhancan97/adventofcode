pairs = 0 # number of pairs that will fully contain the other
with open('assignment.txt', 'r', encoding="utf-8") as f: # Open the file
    assignment = f.readlines() # Read the lines of the file
    assignment = [line.strip() for line in assignment] # Remove the newline character from each line

    for line in assignment:
        # delete the '-' and ',' and split the line into two parts
        line = line.replace('-', ' ').replace(',', ' ').split()
        # convert the strings to integers
        line = [int(i) for i in line]
        # check if the first and second number are in the third and fourth number or third and fourth number are in the first and second number
        if (line[0] <= line[2] and line[1] >= line[2] and line[0] <= line[3] and line[1] >= line[3]) or (line[2] <= line[0] and line[3] >= line[0] and line[2] <= line[1] and line[3] >= line[1]):
            pairs += 1
    
    print(pairs)
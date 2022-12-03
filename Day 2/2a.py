score = 0 # Set score to 0 (this is the variable we will use to store the score)
with open('strategy.txt', 'r', encoding="utf-8") as f: # Open the file
    lines = f.readlines() # Read the lines

    for line in lines: # For each line

        if line[2] == 'X': # If we play rock
            score += 1
        elif line[2] == 'Y': # If we play paper
            score += 2
        elif line[2] == 'Z': # If we play scissors
            score += 3
        
        if (line[0] == 'A' and line[2] == 'X') or (line[0] == 'B' and line[2] == 'Y') or (line[0] == 'C' and line[2] == 'Z'): # If draw
            score += 3
        else:
            if line[0] == 'A' and line[2] == 'Y': # If we play paper and they play rock
                score += 6
            elif line[0] == 'A' and line[2] == 'Z': # If we play scissors and they play rock
                pass
            elif line[0] == 'B' and line[2] == 'X': # If we play rock and they play paper
                pass
            elif line[0] == 'B' and line[2] == 'Z': # If we play scissors and they play paper
                score += 6
            elif line[0] == 'C' and line[2] == 'X': # If we play rock and they play scissors
                score += 6
            elif line[0] == 'C' and line[2] == 'Y': # If we play paper and they play scissors
                pass

print(score) # Print the score
score = 0 # Set score to 0 (this is the variable we will use to store the score)
with open('strategy.txt', 'r', encoding="utf-8") as f: # Open the file
    lines = f.readlines() # Read the lines

    for line in lines: # For each line

        if line[2] == 'X': # If we loose
            score += 0
            if line[0] == 'A': # If opponent plays rock, so we play scissors
                score += 3
            elif line[0] == 'B': # If opponent plays paper, so we play rock
                score += 1
            elif line[0] == 'C': # If opponent plays scissors, so we play paper
                score += 2
        elif line[2] == 'Y': # If we draw
            score += 3
            if line[0] == 'A': # If opponent plays rock, so we play rock
                score += 1
            elif line[0] == 'B': # If opponent plays paper, so we play paper
                score += 2
            elif line[0] == 'C': # If opponent plays scissors, so we play scissors
                score += 3
        elif line[2] == 'Z': # If we win
            score += 6
            if line[0] == 'A': # If opponent plays rock, so we play paper
                score += 2
            elif line[0] == 'B': # If opponent plays paper, so we play scissors
                score += 3
            elif line[0] == 'C': # If opponent plays scissors, so we play rock
                score += 1 
print(score) # Print the score
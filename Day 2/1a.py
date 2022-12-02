import pandas as pd # Import pandas

score = 0
with open('strategy.txt', 'r', encoding="utf-8") as f: # Open the file
    lines = f.readlines() # Read the lines

    for line in lines: # For each line

        if line[2] == 'X':
            score += 1
        elif line[2] == 'Y':
            score += 2
        elif line[2] == 'Z':
            score += 3
        
        if (line[0] == 'A' and line[2] == 'X') or (line[0] == 'B' and line[2] == 'Y') or (line[0] == 'C' and line[2] == 'Z'):
            score += 3
        else:
            if line[0] == 'A' and line[2] == 'Y':
                score += 6
            elif line[0] == 'A' and line[2] == 'Z':
                pass
            elif line[0] == 'B' and line[2] == 'X':
                pass
            elif line[0] == 'B' and line[2] == 'Z':
                score += 6
            elif line[0] == 'C' and line[2] == 'X':
                score += 6
            elif line[0] == 'C' and line[2] == 'Y':
                pass

print(score)
with open('buffer.txt', 'r', encoding="utf-8") as f: # Open the file
    buffer = f.readlines() # Read the lines of the file
    buffer = buffer[0] # Get the actual line
    # loop over the each element of the buffer

    for i in range(len(buffer)-14): # -14 because the last 14 characters are "end"
        s = buffer[i:i+14] # Get the next 14 characters
        if len(set(list(s))) == 14: # If there are 14 different characters (set removes duplicates)
            print(i + 14) # Print the position of the sequence of 14 characters that are all different
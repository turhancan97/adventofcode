with open('buffer.txt', 'r', encoding="utf-8") as f: # Open the file
    buffer = f.readlines() # Read the lines of the file
    buffer = buffer[0] # Get the actual line
    # loop over the each element of the buffer

    for i in range(len(buffer)-3): # -3 because the last 3 characters are "end"
        # indicate the sequence of four characters that are all different and find its position
        if (buffer[i] != buffer[i+1]) and (buffer[i] != buffer[i+2]) and (buffer[i] != buffer[i+3]): # If the three other characters are all different from first character
            if (buffer[i+1] != buffer[i+2]) and (buffer[i+1] != buffer[i+3]): # If the two other characters are all different from second character
                if (buffer[i+2] != buffer[i+3]): # If the other character is different from third character
                    print(i+4) # Print the position of the sequence of four characters that are all different
                    break # Break the loop

                    
                    
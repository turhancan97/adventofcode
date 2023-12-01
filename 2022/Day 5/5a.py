N=9

# Opening the file, reading the lines of the file, removing the newline character from each line, and
# creating a list of lists.
with open('stack.txt', 'r', encoding="utf-8") as f: # Open the file
    stack = f.readlines() # Read the lines of the file
    stack = [line.strip() for line in stack] # Remove the newline character from each line
    S = [[] for _ in range(N)]
    
    # To save each colums of a stack to a list
    for i in range(N-1): # N-1 because the last line is empty
        line = stack[i] # Get the line
        crates = line[1::4] # Get the crates
        for s in range(len(crates)): # For each crate
            if crates[s] != " ": # If the crate is not empty
                S[s].append(crates[s]) # Add the crate to the list

    # Reverse all stacks
    stacks = [stack[::-1] for stack in S] 

    # Move crates one by one
    for line in stack[N+1:]: # N+1 because the first N lines are the stacks
        tokens = line.split(" ") # Split the line
        n, src, dst = map(int, [tokens[1], tokens[3], tokens[5]]) # Get the number of crates, the source, and the destination
        src -= 1 # Subtract 1 because the stacks are 0-indexed
        dst -= 1 # Subtract 1 because the stacks are 0-indexed

        for _ in range(n): # For each crate
            pop = stacks[src].pop() # Pop the crate from the source
            stacks[dst].append(pop) # Add the crate to the destination
    
    tops = [stack[-1] for stack in stacks] # Get the top of each stack
    print("".join(tops)) # Print the top of each stack
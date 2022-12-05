N=9

# Opening the file, reading the lines of the file, removing the newline character from each line, and
# creating a list of lists.
with open('stack.txt', 'r', encoding="utf-8") as f: # Open the file
    stack = f.readlines() # Read the lines of the file
    stack = [line.strip() for line in stack] # Remove the newline character from each line
    S = [[] for _ in range(N)]
    
    # To save each colums of a stack to a list
    for i in range(N-1):
        line = stack[i]
        crates = line[1::4]
        for s in range(len(crates)):
            if crates[s] != " ":
                S[s].append(crates[s])

    # Reverse all stacks
    stacks = [stack[::-1] for stack in S]

    # Move things around
    for line in stack[N+1:]:
        tokens = line.split(" ")
        n, src, dst = map(int, [tokens[1], tokens[3], tokens[5]])
        src -= 1
        dst -= 1

        for _ in range(n):
            pop = stacks[src].pop()
            stacks[dst].append(pop)
    
    tops = [stack[-1] for stack in stacks]
    print("".join(tops))
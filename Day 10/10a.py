with open('instructions.txt', 'r', encoding="utf-8") as f: # Open the file
    lines = f.readlines() # Read the lines of the file
    lines = [line.strip() for line in lines] # Remove the newline character from each line
    
    ans = 0 # initialize the values
    cycle = 0 # initialize the cycle
    X = 1 # initialize the X
    cycle_list = list(range(20,221,40)) # Our cycles that will be used to calculate the answer

    # This is the main loop that is going through the instructions.txt file.
    for line in lines: 
        if line == "noop": # If the line is "noop" then we just increment the cycle
            cycle += 1
            # print(line)
            if cycle in cycle_list: # If the cycle is in the cycle_list then we add the answer
                print(X,cycle,line)
                ans += X * cycle 
        else: # If the line is not "noop" then we have to do some calculations
            ins, value = line.split(" ") # Split the line into the instruction and the value
            # print(ins, value) 
            cycle += 1 # Increment the cycle
            if cycle in cycle_list:  # If the cycle is in the cycle_list then we add the answer
                print(X,cycle,line)
                ans += X * cycle
            cycle += 1 # Increment the cycle
            if cycle in cycle_list: # If the cycle is in the cycle_list then we add the answer
                print(X,cycle,line)
                ans += X * cycle
            X += int(value)

print(cycle_list)
print(ans)

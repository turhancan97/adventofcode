with open('instructions.txt', 'r', encoding="utf-8") as f: # Open the file
    lines = f.readlines() # Read the lines of the file
    lines = [line.strip() for line in lines] # Remove the newline character from each line
    
    ans = 0
    cycle = 0
    X = 1
    cycle_list = list(range(20,221,40))

    for line in lines:
        if line == "noop":
            cycle += 1
            # print(line)
            if cycle in cycle_list:
                print(X,cycle,line)
                ans += X * cycle
        else:
            ins, value = line.split(" ")
            # print(ins, value)
            cycle += 1
            if cycle in cycle_list:
                print(X,cycle,line)
                ans += X * cycle
            cycle += 1
            if cycle in cycle_list:
                print(X,cycle,line)
                ans += X * cycle
            X += int(value)

print(cycle_list)
print(ans)

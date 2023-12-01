import numpy as np

with open('tree_grid.txt', 'r', encoding="utf-8") as f: # Open the file
    matrix = f.readlines() # Read the lines of the file
    matrix = [line.strip() for line in matrix] # Remove the newline character from each line

    grid = [list(map(int, list(line))) for line in matrix]
    grid = np.array(grid) # Convert the list of lists to a numpy array

    nrows, ncols = grid.shape # Get the number of rows and columns
    count = 0 # Initialize the count of trees that are visible
    for i in range(nrows):
        for j in range(ncols):
            tree = grid[i, j] # Get the value of the tree at the current position
            if j == 0 or np.amax(grid[i, :j]) < tree:
                count += 1
            elif j == ncols - 1 or np.amax(grid[i, (j+1):]) < tree: 
                count += 1
            elif i == 0 or np.amax(grid[:i, j]) < tree:
                count += 1
            elif i == nrows - 1 or np.amax(grid[(i+1):, j]) < tree:
                count += 1

print(count)
                
              



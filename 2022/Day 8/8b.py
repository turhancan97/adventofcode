import numpy as np

with open('tree_grid.txt', 'r', encoding="utf-8") as f: # Open the file
    matrix = f.readlines() # Read the lines of the file
    matrix = [line.strip() for line in matrix] # Remove the newline character from each line

    grid = [list(map(int, list(line))) for line in matrix]
    grid = np.array(grid) # Convert the list of lists to a numpy array

    n = len(grid)
    m = len(grid[0])    
    
    dd = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    ans = 0
    for i in range(n):
        for j in range(m):
            h = grid[i, j]
            score = 1

            # Scan in 4 directions
            for di, dj in dd:
                ii, jj = i + di, j + dj
                dist = 0

                while (0 <= ii < n and 0 <= jj < m) and grid[ii, jj] < h:
                    dist += 1
                    ii += di
                    jj += dj

                    if (0 <= ii < n and 0 <= jj < m) and grid[ii, jj] >= h:
                        dist += 1

                score *= dist

            ans = max(ans, score)


    print(ans)
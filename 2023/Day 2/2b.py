with open("games.txt", "r", encoding="utf-8") as f:  # Open the file
    lines = f.readlines()  # Read the lines

cube_temp = {"red": 0, "green": 0, "blue": 0}  # The set of colors

count = 0  # The sum of number of games
power = 1
for line in lines:  # For each line
    # example line: Game 1: 1 blue, 8 green; 14 green, 15 blue; 3 green, 9
    # blue; 8 green, 8 blue, 1 red; 1 red, 9 green, 10 blue
    game_id = int(line.split(":")[0][4:])
    line = line.split(":")[1].strip()
    # split the line into a list of each cube
    cubes = line.split(";")
    # iterate through each cube
    for cube in cubes:
        # set the flag to false
        flag = False
        # remove commas
        cube = cube.replace(",", "")
        # split the cube into a list of the number and color
        cube = cube.split()
        # iterate through each number and find its color
        for i in range(len(cube)):
            if i % 2 == 0:
                # if the number is greater than the maximum number of the
                # color, set the flag to true and break
                if int(cube[i]) > cube_temp[cube[i + 1]]:
                    cube_temp[cube[i + 1]] = int(cube[i])
    # multiply the number of each color
    for color in cube_temp:
        power *= cube_temp[color]
    count += power
    power = 1
    cube_temp = {"red": 0, "green": 0, "blue": 0}  # The set of colors

# print the result
# To calculate the total number of games, we can use the formula: 1+2+3+...+99+100 = 5050
# To calculate valid games, we can subtract the count from the total number of games
print("Sum of the power of these sets: {}".format(count))

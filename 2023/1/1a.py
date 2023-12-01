with open("calibration_document.txt", "r", encoding="utf-8") as f:  # Open the file
    lines = f.readlines()  # Read the lines

list_of_numbers_each_line = []  # Create an empty list to store the numbers for each line
list_of_numbers = []  # Create an empty list to store the numbers
for line in lines:  # For each line
    # go through each character in the line
    for character in line:
        # if the character is a number
        if character.isdigit():
            # add it to the list of numbers
            list_of_numbers_each_line.append(int(character))
    # add the list of numbers for each line to the list of numbers
    list_of_numbers.append(list_of_numbers_each_line)
    # reset the list of numbers for each line
    list_of_numbers_each_line = []

count = 0  # Create a variable to store the count
# itarate through the list of numbers
for number in list_of_numbers:
    # take the first number and last number and add them together
    count = count + int(f"{str(number[0])}" + f"{str(number[-1])}")

print('The sum of all of the calibration values:', count)  # Print the count

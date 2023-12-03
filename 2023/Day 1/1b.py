with open("calibration_document.txt", "r", encoding="utf-8") as f:  # Open the file
    lines = f.readlines()  # Read the lines

list_of_numbers_each_line =[]  # Create an empty list to store the numbers for each line
list_of_numbers = []  # Create an empty list to store the numbers
for line in lines:  # For each line
    # replace 'one' with '1'
    line = line.replace("one", "o1e")
    # replace 'two' with '2'
    line = line.replace("two", "t2o")
    # replace 'three' with '3'
    line = line.replace("three", "th3ee")
    # replace 'four' with '4'
    line = line.replace("four", "fo4r")
    # replace 'five' with '5'
    line = line.replace("five", "fi5e")
    # replace 'six' with '6'
    line = line.replace("six", "s6x")
    # replace 'seven' with '7'
    line = line.replace("seven", "se7en")
    # replace 'eight' with '8'
    line = line.replace("eight", "ei8ht")
    # replace 'nine' with '9'
    line = line.replace("nine", "ni9e")
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
    if number:
        # take the first number and last number and add them together
        count = count + int(f"{str(number[0])}" + f"{str(number[-1])}")

print("The sum of all of the calibration values:", count)  # Print the count
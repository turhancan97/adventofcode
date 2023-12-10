# Open the file and read all lines
with open("race.txt", "r") as file:
    lines = file.readlines()

record_dict = {}
for line in lines:
    line = line.strip().split(" ")
    # delete all element containing ""
    while "" in line:
        line.remove("")
    record_dict[line[0]] = line[1:]

# turn the values into integers
for key in record_dict:
    for i in range(len(record_dict[key])):
        record_dict[key][i] = int(record_dict[key][i])

count = 0  # count the number of recordsx
record_list = []  # store the records
for value in range(len(record_dict["Time:"])):
    for hold in range(0, record_dict["Time:"][value] + 1):
        move = record_dict["Time:"][value] - hold
        speed = move * hold
        if speed > record_dict["Distance:"][value]:
            count += 1
    record_list.append(count)
    count = 0

# print the result
print("Number of ways you can beat the record", record_list)
# Multiply the numbers in the list
result = 1
for i in record_list:
    result = result * i
print("Multiplication of all the numbers in the list", result)

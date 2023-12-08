# Open the file and read all lines
with open("race.txt", "r") as file:
    lines = file.readlines()

record_dict = {}
for line in lines:
    line = line.strip().split(" ")
    # delete all element containing ""
    while "" in line:
        line.remove("")
    # connect all the strings in the list
    values = "".join(line[1:])
    values = int(values)
    record_dict[line[0]] = [values]

count = 0  # count the number of records
record_list = []  # store the records
# calculate the number of records
# Example record_dict -> {'Time:': [71530], 'Distance:': [940200]}
for time, distance in zip(record_dict["Time:"], record_dict["Distance:"]):
    count = 0
    for hold in range(time + 1):
        move = time - hold
        speed = move * hold
        if speed > distance:
            count += 1
    record_list.append(count)

# print the result
print("Number of ways you can beat the record", record_list[0])

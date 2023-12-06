# Open the file and read the lines
file = open("almanac.txt", "r")
lines = file.readlines()
file.close()

# Process the seeds
seeds_line = lines[0].strip().split(": ")[1]
seeds = seeds_line.split(" ")
for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

# Process the mappings
mappings = []
for line in lines[2:]:
    line = line.strip()
    if line.endswith(":"):
        mappings.append([])
    elif len(line) > 0:
        numbers = line.split(" ")
        int_numbers = []
        for num in numbers:
            int_numbers.append(int(num))
        mappings[-1].append(int_numbers)

# Sort the mappings
for m in mappings:
    m.sort(key=lambda x: x[1])

# Find the lowest location number
res = 2**32
for x in seeds:
    for typemappings in mappings:
        for mapping in typemappings:
            if x >= mapping[1] and x < mapping[1] + mapping[2]:
                x = x - mapping[1] + mapping[0]
                break
    if x < res:
        res = x

# Print the result
print("Lowest location number that corresponds to any of the initial seed numbers?", res)
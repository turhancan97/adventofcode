with open("almanac.txt", "r") as file:
    lines = file.readlines()

seeds = []
for i in lines[0].strip().split(": ")[1].split(" "):
    seeds.append(int(i))

mappings = []
for line in lines[2:]:
    line = line.strip()
    if line.endswith(":"):
        mappings.append([])
    elif len(line) > 0:
        mappings[-1].append([int(i) for i in line.split(" ")])

[m.sort(key=lambda x: x[1]) for m in mappings]

res = 2**32
for x in seeds:
    for typemappings in mappings:
        for mapping in typemappings:
            if x >= mapping[1] and x < mapping[1] + mapping[2]:
                x = x - mapping[1] + mapping[0]
                break
    res = min(x, res)
print(
    "Lowest location number that corresponds to any of the initial seed numbers?", res
)

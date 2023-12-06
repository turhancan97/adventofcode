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

res = 2**64
for s, o in zip(seeds[::2], seeds[1::2]):
    ranges = [(s, s + o - 1)]
    for typemappings in mappings:
        newranges = []
        for l, h in ranges:
            found = False
            for md, ms, mo in typemappings:
                if l >= ms and h < ms + mo:
                    newranges.append((l - ms + md, h - ms + md))
                    found = True
                elif l < ms and h >= ms and h < ms + mo:
                    ranges.append((l, ms - 1))
                    newranges.append((md, md + h - ms))
                    found = True
                elif l < ms + mo and h >= ms + mo and l >= ms:
                    ranges.append((ms + mo, h))
                    newranges.append((md + l - ms, md + mo - 1))
                    found = True
                elif l < ms and h >= ms + mo:
                    ranges.append((l, ms - 1))
                    newranges.append((md, md + mo - 1))
                    ranges.append((ms + mo, h))
                    found = True
                if found == True:
                    break
            if found == False:
                newranges.append((l, h))
        ranges = newranges.copy()
    res = min(res, min(ranges)[0])
print(
    "Lowest location number that corresponds to any of the initial seed numbers?", res
)

from collections import defaultdict

with open("engine_schematic.txt", "r", encoding="utf-8") as f:  # Open the file
    lines = f.read().strip().split("\n")

G = [[c for c in line] for line in lines]  # The grid
R = len(G)  # Number of rows
C = len(G[0])  # Number of columns

sum_gear_ratios = 0  # The sum of all of the gear ratios
nums = defaultdict(list)  # The numbers on the gears
for r in range(len(G)):
    gears = set()  # positions of '*' characters next to the current number
    n = 0
    has_part = False
    for c in range(len(G[r]) + 1):
        if c < C and G[r][c].isdigit():
            n = n * 10 + int(G[r][c])
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0 <= r + rr < R and 0 <= c + cc < C:
                        ch = G[r + rr][c + cc]
                        if not ch.isdigit() and ch != ".":
                            has_part = True
                        if ch == "*":
                            gears.add((r + rr, c + cc))
        elif n > 0:
            for gear in gears:
                nums[gear].append(n)
            if has_part:
                sum_gear_ratios += n
            n = 0
            has_part = False
            gears = set()

print('Sum of all of the gear ratios: ', sum_gear_ratios)
sum_gear_ratios_p2 = 0
for k, v in nums.items():
    if len(v) == 2:
        sum_gear_ratios_p2 += v[0] * v[1]
print('Sum of all of the gear ratios: ', sum_gear_ratios_p2)

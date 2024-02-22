with open("history.txt", "r") as f:
    lines = f.read()

total = 0
for line in lines.split("\n"):
    nums = [int(n) for n in line.split()]
    final_nums = []
    while set(nums) != set([0]):
        final_nums.append(nums[-1])
        nums = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

    total += sum(final_nums)

print("Sum of the extrapolated values: ", total)
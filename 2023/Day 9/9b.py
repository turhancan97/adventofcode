with open("history.txt", "r") as f:
    lines = f.read()

total = 0
for line in lines.split("\n"):
    nums = [int(n) for n in line.split()]
    first_nums = []

    while set(nums) != set([0]):
        first_nums.append(nums[0])
        nums = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

    for i, num in enumerate(first_nums):
        total += num if i % 2 == 0 else -num

print("Sum of the extrapolated values: ", total)

length = 50

file = open('input/input13.txt', 'r')

nums = []
for line in file:
    nums.append(int(line))

print(str(sum(nums))[:10])
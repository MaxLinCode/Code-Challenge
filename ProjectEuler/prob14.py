# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

maxCount = -1
maxStartNum = -1

for i in range(999999,0,-1):
    x = i
    count = 1
    while x != 1:
        if x%2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        count += 1
    if count > maxCount:
        maxCount = count
        maxStartNum = i

print (maxStartNum)
print (maxCount)
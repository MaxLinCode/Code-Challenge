i = 1
j = 2
sum = 0
while i < 4000000:
    temp = i
    i = j
    j += temp
    if i % 2 == 0:
        sum += i

print (sum)

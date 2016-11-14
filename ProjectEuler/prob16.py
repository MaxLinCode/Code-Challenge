def sumDigits(x):
    strX = str(x)
    sum = 0
    for c in strX:
        sum += int(c)

    return sum

print (sumDigits(2**1000))
def isPrime(n):
    for i in range(2, int(n**(0.5))+1):
        if (n%i == 0):
            return False;

    return True;

# start at 2 and 3
sum = 2 + 3
i = 1

while i < 2000000:
    # i6 = i * 6
    # if (isPrime(i6 - 1)):
    #     sum += i6 - 1
    # if (isPrime(i6 + 1)):
    #     sum += i6 - 1
    if (isPrime(i)):
        sum += i
    i += 1
    print(i)

print (sum)

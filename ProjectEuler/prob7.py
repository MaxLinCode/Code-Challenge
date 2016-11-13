def isPrime(n):
    for i in range(2, int(n**(0.5))+1):
        if (n%i == 0):
            return False;
    
    return True;

max = 0
i = 1
j = 2
while i <= 10001:    
    if isPrime(j):
        max = j
        i += 1
    j += 1

print (max)

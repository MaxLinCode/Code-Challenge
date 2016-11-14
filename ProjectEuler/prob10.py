import time

def isPrime(n):
    for i in range(2, int(n**(0.5))+1):
        if (n%i == 0):
            return False;

    return True;

def sumPrimeStep1(n):
    total = 0 
    i = 2

    while i < n:
        if (isPrime(i)):
            total += i
        i += 1

    return total

def sumPrimeStep6(n):
    total = 2 + 3
    i = 6

    while i < n:
        if isPrime(i+1):
            total += i+1
        if isPrime(i-1):
            total += i-1
        i += 6

    return total

num = 5000000
t1 = time.process_time()
print(sumPrimeStep1(num))
print (time.process_time() - t1)

t2 = time.process_time()
print(sumPrimeStep6(num))
print(time.process_time() - t2)


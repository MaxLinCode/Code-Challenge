import math
num = 600851475143 
factor = 1
i = 0

def hasPrimeForm(num):
    return ((num+1)%6 == 0 or (num-1)%6 == 0)
def nextPrime(lastPrime):
    i = lastPrime
    while True:
        i += 1
        if (hasPrimeForm(i)):
            sqrtNum = math.sqrt(i)
            factor = 2
            while factor <= sqrtNum:
                if hasPrimeForm(factor) and i % factor  == 0:
                    break
                factor += 1
            else:
                return i

def largestPrimeFactor():
    






import math
def sumProperDivisors(n):
    # account for divisor of 1 excluding itself
    total = 1
    nSqrt = int(math.sqrt(n))
    for index in range(2, nSqrt + 1):
        if n % index == 0:
            total += index + int(n / index)

    # account for perfect square
    if nSqrt**2 == n:
        total -= nSqrt

    return total

# n is the upper bound
def sumAmicableNumbers(n):
    total = 0
    prevAmicable = -1
    for a in range(1, n):
        b = sumProperDivisors(a)
        bdivs = sumProperDivisors(b)
        if b > a and bdivs == a:
            total += b + bdivs
            prevAmicable = b
            print(a)
            print(b)

    return total

print(sumAmicableNumbers(10000))

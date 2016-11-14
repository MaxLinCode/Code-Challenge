def factorial(n):
    prod = 1
    for i in range(n, 1, -1):
        prod *= i

    return prod

def prodDigits(strNum):
    product = 1
    for i in range(len(strNum)):
        product *= int(strNum[i])

    return product

def factorialDigitSum(n):
    total = 0
    num = factorial(n)
    strNum = str(num)
    for i in range(len(strNum)):
        total += int(strNum[i])

    return total

print (factorialDigitSum(100))


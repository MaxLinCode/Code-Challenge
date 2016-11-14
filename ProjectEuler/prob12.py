import math

def numDivisors(x):
    # account for divisor of 1 and itself
    count = 2
    # highest divisor is half of itself
    root = math.sqrt(x)
    for index in range(2,int(root+1)):
        if x % index == 0:
            count += 2
    
    if root == int(root):
        # adjust if num is perfect square
        count -= 1

    # each divisor has pair
    return count

lastTri = 0
num = 0

i = 1
while True:
    num = lastTri + i
    lastTri = num
    if (numDivisors(num) > 500):
        print(num)
        break
        
    i += 1
def isPalindrome(num):
    return str(num) == str(num)[::-1]

maxPal = 0
for i in range(0,1000):
    for j in range(0,1000):
        if(isPalindrome(i*j) and i*j >  maxPal):
            maxPal = i*j

print (maxPal)

n = 100 

# x is sum of 2 middle term
#i = 0
#end = int((n/2)-1)
#x = int(n/2)**2 + (int(n/2)+1)**2
#squaresSum = 0
#while i <= end:
#    squaresSum += x + 4 * i
#    x = x + 4
#    i += 1

#z = (n/2)**2 + ((n/2)+1)**2  
#totalDiff = ((n/2)*4/2)*4
#print (totalDiff)
#print((z*n/2)-totalDiff)

i = 1
squaresSum = 0
while i <= n:
    squaresSum += i**2
    i += 1

print (squaresSum)

sumSquared = ((n*(n+1))/2)**2


print (sumSquared)

print (str(sumSquared - squaresSum))

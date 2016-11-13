import math
a = 1
b = 1

for a in range(1,1000):
    for b in range(1,1000):
        c = math.sqrt(a**2 + b**2)
        if (b > a and c.is_integer()):
            if(a + b + c == 1000):
                print (str(a) + " " + str(b))
                print (a * b * c) 
                exit()

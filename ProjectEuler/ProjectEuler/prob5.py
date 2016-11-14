i = 1 
while True:
    for j in range(20,10,-1):
        if (i % j != 0):
            break
    else:
        print (i)
        break
    i += 1

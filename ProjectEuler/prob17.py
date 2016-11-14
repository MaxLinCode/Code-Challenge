ones = ["", "one", "two","three", "four", "five", "six", "seven", "eight", "nine", "ten"]
elevens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
digitArr = [ones, tens]
total = 0
for i in range(1,1001):
    x = i
    print(i)
    while True:
        if x >= 1000:
            total += len(ones[int(x/1000)]) + len("thousand")
            if int(str(x)[1:]) != 0:
                # stupid british convention
                total += len("and")
            print(str(ones[int(x/1000)]) + "-" + "thousand")
        elif x >= 100:
            total += len(ones[int(x/100)]) + len("hundred")
            if int(str(x)[1:]) != 0:
                # stupid british convention
                total += len("and")
            print(str(ones[int(x/100)]) + "-" + "hundred")
        elif x >= 20:
            total += len(tens[int(x/10)])
            print(tens[int(x/10)])
        elif x > 10:
            total += len(elevens[x-10])
            print(elevens[x-10])
            break
        elif x == 10:
            total += len("ten")
            print("ten")
            break
        elif x > 0:
            total += len(ones[x])
            print(ones[x])

        nextXstr = str(x)[1:]
        if nextXstr == "":
            break
        else:
            x = int(nextXstr)

print(total)

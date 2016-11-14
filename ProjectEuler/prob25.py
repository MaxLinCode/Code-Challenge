i = 1
last = 0
curr = 1

while len(str(curr)) < 1000:
    temp = curr
    curr += last
    last = temp
    i += 1

print(i)
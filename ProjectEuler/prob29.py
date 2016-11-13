vals = []
for a in range(2,101):
    for b in range(2,101):
        vals.append(a**b)

vals = set(vals)
print (len(vals))

import csv

def insertionSort(list):
    for i in range(1, len(list)): 
        j = i
        currVal = list[j] 
        while j > 0 and list[j-1] > currVal:
            list[j] = list[j-1]
            j -= 1

        list[j] = currVal
                  
    return list

names = []
with open('input/input22_names.txt', 'r') as csvfile:
        myReader = csv.reader(csvfile)
        for row in myReader:
            names = row

sortedNames = sorted(names)
total = 0
for i in range(len(sortedNames)):
    charSum = 0
    for char in sortedNames[i]:
        charSum += ord(char) - 64
    total += (i+1) * charSum

print(total)
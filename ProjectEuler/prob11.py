import numpy as np

# Largest Product in a grid

# n = size of grid
n = 20

grid = np.empty(20*20).reshape(20,20).astype(int)
file = open('input11.txt', 'r')

for i in range(n) :
    line = file.readline().split(" ")
    grid[i] = np.array(list(map(int, line)))

maxProd = -1
# horizontally and vertically
for i in range(n):
    row = grid[i]
    col = grid[i]
    for j in range(0, n, 4):
        prodHori = row[j] * row[j+1] * row[j+2] * row[j+3]
        prodVert = col[j] * col[j+1] * col[j+2] * col[j+3]
        maxProd = max(maxProd, prodHori, prodVert)

    # check first 4 from back if n is not multiple of length
    prodHori = row[n-1] * row[n-2] * row[n-3] * row[n-4]
    prodVert = col[n-1] * col[n-2] * col[n-3] * col[n-4]
    maxProd = max(maxProd, prodHori, prodVert)

# n-4
for row in range(0, n-4):
    for i in range(0, n):
        # diagonal down left
        if not i < 3:
            prod = 1
            for j in range(0, 4):
                prod *= grid[(j+row)][i-j]
            maxProd = max(prod, maxProd)
        # diagonal down right
        if not i + 3 >= n:
            prod = 1
            for j in range(0, 4):
                prod *= grid[j+row][j+i]
            maxProd = max(prod, maxProd)

print (maxProd)


    

        
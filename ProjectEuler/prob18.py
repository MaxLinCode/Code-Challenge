data = []
memo = []
# load the data
with open('input/input18.txt', 'r') as file:
    i = 1
    for line in file:
        data.append(list(map(int, line.split(" "))))
        memo.append([-1 for row in range(i)])
        i += 1

maxDepth = len(data)


def maxPathSum(depth, col): 
    if depth >= maxDepth - 1:
        return data[maxDepth-1][col]
    else:
        if memo[depth][col] == -1:
            memo[depth][col] = data[depth][col] + max(maxPathSum(depth + 1, col), maxPathSum(depth + 1, col + 1))
        return memo[depth][col]

print(maxPathSum(0, 0))
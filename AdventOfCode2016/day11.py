input = open("input11.txt", 'r')


floors = []
for line in input:
    if "nothing" in line:
        floors.append([])
        continue

    chips = []
    gens = []
    asdf = []
    stuff = line[line.index("contains"):].replace("and",",").split(", ")
    for thing in stuff:
        if "microchip" in thing:
            asdf.append(str(thing.split()[-2][:2]) + "m")
        elif "generator" in thing:
            asdf.append(str(thing.split()[-2][:2]) + "g")

    # floors.append(chips + gens)
    floors.append(asdf)

for floor in floors:
    floor = sorted(floor)

print(floors)
numItems = 0
for floor in floors:
    numItems += len(floor)

numItems /= 2
numItems = int(numItems)
numFloors = len(floors)

endNode = ""
for i in range(numItems):
    endNode += str(numFloors-1) + str(numFloors-1)

endNode += str(numFloors-1) 

def stupidPad(num):
    num = num + 10 ** ((numItems*2) + 1)
    return str(num)[1:]

def isPossibleConfig(line):
    line = str(line)[1:]
    for char in line:
        if int(char) >= numFloors:
            return False
    # for each gen
    i = 0
    while i < len(line):
        j = 1
        while j < len(line):
            if line[j] == line[i] and line[j] != line[j-1]:
                return False
            j += 2
        i += 2

    return True


# a and b are strings
def possibleStep(strA,strB):
    # if greater than 1 step
    floorDiff = int(strB[0]) - int(strA[0])
    if abs(floorDiff) != 1:
        return False
    total = 0
    # can only move Stuff on same floor
    canMove = []
    for i in range(len(strA)-1):
        if strA[1:][i] == strA[0]:
            canMove.append(i)

    for i in range(len(strA)-1):
        diff = int(strB[1:][i]) - int(strA[1:][i])
        if i not in canMove and diff != 0:
            return False
        if diff != 0 and diff != floorDiff:
            return False
        total += diff

    return total <= 2 and total > 0

print("Calculating possible states.")
nodes = []
for i in range(int(endNode)+1):
    config = stupidPad(i)
    if isPossibleConfig(config): 
        print(config)
        nodes.append([config,[],False])


startNode = "00000121111"
# startNode = "01020"
print(startNode)
print(endNode)
# put start node at pos 0
for i in range(len(nodes)):
    if nodes[i][0] == startNode:
        nodes[0][0], nodes[i][0] = nodes[i][0], nodes[0][0]
        break

print("Making graph.")
for i in range(len(nodes)):
    a = nodes[i]
    j = i + 1
    #print(i)
    while j < len(nodes):
        b = nodes[j]
        if possibleStep(a[0],b[0]):
            a[1].append(j)
            b[1].append(i)
        j += 1

print("Done making graph.")


def backtrace(parent, start, end):
    path = [nodes[end]]
    print("Backtracing.")
    while path[-1][0] != nodes[start][0]:
        path.append(parent[path[-1][0]])
    path.reverse()
    return path


# Does a breadth first search of a graph
# @param graph list of lists, adjacency list
# @param source int the source node to start the search
# @param target int the target node to search for
def bfs(graph, start, end):
    queue = []
    parent = {}

    for node in range(len(graph)):
        parent[nodes[node][0]] = None

    queue.append(nodes[start])
    while queue:
        current = queue.pop(0)
        if current[0] == nodes[end][0]:
            out = backtrace(parent, start, end)
            print(len(out)-1)
            for h in out:
                print(h[0])
            break

        for neighbor in current[1]:
            if nodes[neighbor][2] == False:
                nodes[neighbor][2] = True
                parent[nodes[neighbor][0]] = current
                queue.append(nodes[neighbor])


bfs(nodes,0,len(nodes)-1)







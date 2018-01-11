import math

class Cell:
    def __init__(self, r = 0, c = 0):
        self.f = 0
        self.g = 0
        self.h = 0
        self.row = r
        self.col = c
        self.parent = None

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __str__(self):
        return "Cell: f = " + str(self.f) + ", r = " + \
               str(self.row) + ", c = " + str(self.col)
    def __repr__(self):
        return self.__str__()

# Manhattan heuristic
def heuristic(start, goal):
    return abs(goal.row - start.row) + abs(goal.col - start.col)

# Shitty linear search to fin the lowest F cost cell
def getLowestCost(olist):
    lowestIndex = 0
    for i in range(1, len(olist)):
        if olist[i].f < olist[lowestIndex].f:
            lowestIndex = i
            
    return lowestIndex

def isValidAndNotAWall(node, grid):
    w = len(grid[0])
    h = len(grid)
    if 0 <= node.col and node.col < w:
        if 0 <= node.row and node.row < h:
            if grid[node.row][node.col] != 'W':
                return True
    return False

def getNeighbors(node, grid):
    r = node.row
    c = node.col
    potential = [Cell(r-1,c),Cell(r+1,c),Cell(r,c-1),Cell(r,c+1)]
    neighbors = [cell for cell in potential if isValidAndNotAWall(cell, grid)]
    for n in neighbors:
        n.g = node.g + 1
        n.parent = node
        
    return neighbors

def construct_path(node):
    path = [node]
    while node.parent:
        node = node.parent
        path = [node] + path

    return path

def print_path(path):
    for x in path:
        print(x.row, " ", x.col)

def AStar(start, goal, grid):
    open_list = [start]
    closed_list = []
    start.g = 0
    start.f = start.g + heuristic(start, goal)
    while open_list != []:
        index = getLowestCost(open_list)
        current = open_list[index]
        if current == goal:
            return current
        open_list = open_list[:index] + open_list[index+1:]
        closed_list.append(current)
        neighbors = getNeighbors(current, grid)
        #print("neighbors: ", neighbors)
        #input()
        for neighbor in neighbors:
            if neighbor not in closed_list:
                neighbor.f = neighbor.g + heuristic(neighbor, goal)
                if neighbor not in open_list:
                    open_list.append(neighbor)
                else:
                    open_neighbor = open_list[open_list.index(neighbor)]
                    if neighbor.g < open_neighbor.g:
                        open_neighbor.g = neighbor.g
                        open_neighbor.parent = neighbor.parent
    return None
                
def gridVal(char):
    if char == 'S':
        return 'S'
    elif char == 'F':
        return 'F'
    elif char == 'W':
        return 'W'
    else:
        return int(char)

fname = "../maps/map1.txt"
w = 0
h = 0
grid = None
start = None
finish = None

with open(fname) as fp:
    w, h = [int(x) for x in next(fp).strip().split()]
    grid = [[gridVal(x) for x in line.strip()] for line in fp]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                start = Cell(r, c)
            elif grid[r][c] == 'F':
                finish = Cell(r, c)

ret = AStar(start, finish, grid)
if ret:
    print("path found")
    path = construct_path(ret)
    print_path(path)
else:
    print("no possible path")

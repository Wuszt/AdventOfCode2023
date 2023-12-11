from enum import Flag, auto
import math

file = open("input.txt", "r")
map = ['x' + x.strip() + 'x' for x in file.readlines()]
map.insert(0, 'x' * len(map[0]))
map.append('x' * len(map[0]))

class Directions(Flag):
    NONE = 0
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()

def GetDirections(pos):
    char = map[pos[1]][pos[0]]
    if char == '|': return Directions.UP | Directions.DOWN
    elif char == '-': return Directions.LEFT | Directions.RIGHT
    elif char == 'L': return Directions.UP | Directions.RIGHT
    elif char == 'J': return Directions.UP | Directions.LEFT
    elif char == '7': return Directions.DOWN | Directions.LEFT
    elif char == 'F': return Directions.DOWN | Directions.RIGHT
    elif char == '.' or char == 'x' : return Directions.NONE
    elif char == 'S': return Directions.LEFT | Directions.RIGHT | Directions.UP | Directions.DOWN
    raise Exception()

def GetOppositeDir(dir):
    if dir == Directions.UP: return Directions.DOWN
    elif dir == Directions.DOWN: return Directions.UP
    elif dir == Directions.LEFT: return Directions.RIGHT
    elif dir == Directions.RIGHT: return Directions.LEFT

def FindStart():
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == 'S':
                return (x,y)
    raise Exception()

def FindConnection(currPos, prevPos):
    dirs = GetDirections(currPos)

    if Directions.UP in dirs:
        pos = (currPos[0], currPos[1] - 1)
        posDirs = GetDirections(pos)
        if Directions.DOWN in posDirs and pos != prevPos: return pos
    
    if Directions.DOWN in dirs:
        pos = (currPos[0], currPos[1] + 1)
        posDirs = GetDirections(pos)
        if Directions.UP in posDirs and pos != prevPos: return pos

    if Directions.LEFT in dirs:
        pos = (currPos[0] - 1, currPos[1])
        posDirs = GetDirections(pos)
        if Directions.RIGHT in posDirs and pos != prevPos: return pos

    if Directions.RIGHT in dirs:
        pos = (currPos[0] + 1, currPos[1])
        posDirs = GetDirections(pos)
        if Directions.LEFT in posDirs and pos != prevPos: return pos

    raise Exception()

def CalcPipes(start):
    pipes = [start]
    pipes.append(FindConnection(start,start))
    while(pipes[-1] != start):
        pipes.append(FindConnection(pipes[-1], pipes[-2]))
    return pipes

def Part1():
    print((len(CalcPipes(FindStart())) - 1) / 2)

def IsPartOfMap(pos):
    inXBorders = pos[0] >= 0 and pos[0] < len(map[0])
    inYBorders = pos[1] >= 0 and pos[1] < len(map)
    return inXBorders and inYBorders

def IsHorizontal(dir):
    return Directions.LEFT in dir or Directions.RIGHT in dir

def IsVertical(dir):
    return Directions.UP in dir or Directions.DOWN in dir

def PopulateNestInternal(pos, pipes, nest, toVisit):
    alreadyInNest = pos in nest
    isPipe = pos in pipes
    if (not IsPartOfMap(pos)) or alreadyInNest or isPipe:
        return

    nest.add(pos)

    toVisit.add((pos[0] + 1, pos[1]))
    toVisit.add((pos[0] - 1, pos[1]))
    toVisit.add((pos[0], pos[1] + 1))
    toVisit.add((pos[0], pos[1] - 1))

def PopulateNest(pos, pipes, nest):
    toVisit = {pos}

    while(len(toVisit) > 0):
        PopulateNestInternal(toVisit.pop(), pipes, nest, toVisit)

def Traverse(pipes, nests):
    maxX = 0
    maxXIndex = 0
    for p, pos in enumerate(pipes):
        if pos[0] > maxX:
            maxX = pos[0]
            maxXIndex = p

    pipe0 = pipes[maxXIndex % len(pipes)]
    pipe1 = pipes[(maxXIndex + 1) % len(pipes)]

    offset = (1,0)

    currDir = (pipe1[0] - pipe0[0], pipe1[1] - pipe0[1])
    for i in range(len(pipes)):
        index = (i + maxXIndex) % len(pipes)
        currPipe = pipes[index]
        nextPipe = pipes[(index + 1) % len(pipes)]
        newDir = (nextPipe[0] - currPipe[0], nextPipe[1] - currPipe[1])

        ppps = []

        ppps.append((currPipe[0] + offset[0], currPipe[1] + offset[1]))

        if newDir != currDir:
            newAngle = math.atan2(offset[1],offset[0]) + math.atan2(newDir[1],newDir[0]) - math.atan2(currDir[1],currDir[0])
            newOffset = [math.cos(newAngle), math.sin(newAngle)]
            newOffset[0] = (1.0 if newOffset[0] > 0.0 else -1.0) * (1 if abs(newOffset[0]) > 0.25 else 0)
            newOffset[1] = (1.0 if newOffset[1] > 0.0 else -1.0) * (1 if abs(newOffset[1]) > 0.25 else 0)

            newHalfOffset = (newOffset[0] + offset[0], newOffset[1] + offset[1])
            ppps.append((currPipe[0] + newHalfOffset[0], currPipe[1] + newHalfOffset[1]))
            
            currDir = newDir
            offset = newOffset
            ppps.append((currPipe[0] + offset[0], currPipe[1] + offset[1]))
        for ppp in ppps:
            for n, nest in enumerate(nests):
                if ppp in nest:
                    del nests[n]
                    break
    sum = 0
    for nest in nests:
        sum += len(nest)
    print(sum)

def Part2():
    pipes = CalcPipes(FindStart())
    pipesSet = set(pipes)
    nests = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if (x,y) in pipes:
                continue

            inAny = False
            for nest in nests:
                if (x,y) in nest:
                    inAny = True
            if not inAny:
                nests.append(set())
                PopulateNest((x,y), pipesSet, nests[-1])
    Traverse(pipes, nests)

Part1()
Part2()
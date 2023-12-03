def IsValidPart1(y, startX, endX, grid):
    for yy in range(y-1,y+2,2):
        for x in range(startX-1, endX+1):
            if grid[yy][x] != '.':
                return True
    return grid[y][startX-1] != '.' or grid[y][endX] != '.'

lines = [x.strip() for x in open("input.txt", "r").readlines()]
rowLength = len(lines[0]) + 2
grid, gears, nrs, sums = ['.' * rowLength], [], {}, [0,0] 
for line in lines:
    grid.append('.' + line.strip() + '.')
grid.append("." * rowLength)

for y in range(len(grid)):
    start, nr = rowLength, 0
    for x in range(rowLength):
        if grid[y][x] >= '0' and grid[y][x] <= '9':
            nr = nr * 10 + int(grid[y][x])
            start = min(start, x)
        else:
            if start != rowLength and IsValidPart1(y, start, x, grid): sums[0] += nr
            if grid[y][x] == '*': gears.append([y,x])
            if start != rowLength:
                for xx in range(start, x):
                    nrs[(y,xx)] = nr
            start, nr = rowLength, 0

for gear in gears:
    localNrs = [[-1,-1]]
    for y in range(gear[0] - 1, gear[0] + 2):
        for x in range(gear[1] - 1, gear[1] + 2):
            if (y,x) in nrs and (nrs[(y,x)] != localNrs[-1][1] or localNrs[-1][0] != y):
                localNrs.append([y,nrs[(y,x)]])
    if len(localNrs) == 3: sums[1] += localNrs[1][1] * localNrs[2][1]
print(sums)
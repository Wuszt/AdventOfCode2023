def Calc(emptySpaceMultiplier):
    grid = [x.strip() for x in open("input.txt", "r").readlines()]

    galaxies = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '#':
                galaxies.append((x,y))

    emptyRows, emptyCollumns = [], []

    for y in range(len(grid)):
        anyInRow = False
        for galaxy in galaxies:
            anyInRow |= galaxy[1] == y
        if not anyInRow:
            emptyRows.append(y)

    for x in range(len(grid[0])):
        anyInCollumn = False
        for galaxy in galaxies:
            anyInCollumn |= galaxy[0] == x
        if not anyInCollumn:
            emptyCollumns.append(x)

    for g, galaxy in enumerate(galaxies):
        galaxies[g] = (galaxy[0] + sum((emptySpaceMultiplier-1) for x in emptyCollumns if x < galaxy[0]), galaxy[1] + sum((emptySpaceMultiplier-1) for x in emptyRows if x < galaxy[1]))

    s = 0
    for g, galaxy in enumerate(galaxies):
        for g1 in range(g, len(galaxies)):
            s += abs(galaxies[g][0] - galaxies[g1][0]) + abs(galaxies[g][1] - galaxies[g1][1])
    return s

print((Calc(2), Calc(1000000)))
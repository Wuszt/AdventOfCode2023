def Calc(seeds):
    result = 99999999999
    for s in range(0,len(seeds),2):
        ranges = [[seeds[s], seeds[s] + seeds[s+1] - 1]]
        for map in maps:
            i = -1
            while(i + 1 < len(ranges)):
                i += 1
                for r in map:
                    sMin, sMax, rMin, rMax = ranges[i][0], ranges[i][1], r[1], r[1] + r[2] - 1
                    if sMin >= rMin and sMin <= rMax and sMax > rMax:
                        ranges[i][1] = rMax
                        ranges.append([rMax + 1, sMax])
                    elif sMin < rMin and sMax >= rMin:
                        ranges[i][0] = rMin
                        ranges.append([sMin, rMin - 1])
                        if sMax > rMax:
                            ranges[i][1] = rMax
                            ranges.append([rMax + 1, sMax])

                    if ranges[i][0] >= rMin and ranges[i][1] <= rMax:
                        ranges[i] = [ranges[i][0] - r[1] + r[0], ranges[i][1] - r[1] + r[0]]
                        break
        for ran in ranges: result = min(ran[0], result)
    return result

file = open("input.txt", "r")
line = file.readline()
file.readline()
seeds = [int(x) for x in line[line.index(':') + 1:].strip().split(' ')]
maps = []
for x in file:
    line = file.readline()
    maps.append([])
    while(line != ''):
        maps[-1].append([int(x) for x in line.split(' ')])
        line = file.readline().strip()

print((Calc([i for s in ([x] + [1] for x in seeds) for i in s]), Calc(seeds)))
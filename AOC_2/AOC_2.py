sums = [0,0]
for line in [[i,line[line.index(':') + 1:].split(';')] for i, line in enumerate(open("i.txt", "r"))]:
    clrs = {"red": 0, "green": 0, "blue": 0}
    for s in line[1]:
        for cube in [x.split(' ') for x in [x.strip() for x in s.split(',')]]:
            clrs[cube[1]] = max(clrs[cube[1]], int(cube[0]))
    sums[0] += (0 if (clrs["red"] > 12 or clrs["green"] > 13 or clrs["blue"] > 14) else (line[0] + 1))
    sums[1] += clrs["red"] * clrs["green"] * clrs["blue"]
print(sums)
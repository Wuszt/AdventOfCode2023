lines = open("input.txt", "r").readlines()
crds, sums = [1] * len(lines), [0,0]
for i, nr in enumerate([x[x.index(':')+1:].rstrip().split('|') for x in lines]):
    my = [x for x in nr[1].strip().split(' ') if x != '' and x in nr[0].strip().split(' ')]
    for o in range(len(my)): crds[i + o + 1] += crds[i]
    sums = [sums[0] + int(pow(2,len(my) - 1)), sums[1] + crds[i]]
print(sums)
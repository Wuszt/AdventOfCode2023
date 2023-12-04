lines = open("input.txt", "r").readlines()
crds = [1] * len(lines)
sums = [0,0]
for i, nr in enumerate(nr.split('|') for nr in [x[x.index(':')+1:].rstrip() for x in lines]):
    winners = nr[0].strip().split(' ')
    my = [x for x in nr[1].strip().split(' ') if x != '']
    offset = 1
    for m in my:
        if m in winners:
          crds[i + offset] += 1 * crds[i]
          offset += 1
    sums = [sums[0] + (pow(2,offset - 2) if offset > 1 else 0), sums[1] + crds[i]]
print(sums)
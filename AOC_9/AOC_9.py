def Populate(values):
    values.append([])

    for i in range(len(values[-2]) - 1):
        values[-1].append(values[-2][i + 1] - values[-2][i])

    for val in values[-1]:
        if val != 0:
            Populate(values)
            break

def Calc(lines):
    s = 0
    for line in lines:
        values = [line]
        Populate(values)
        for val in values:
            s += val[-1]
    return s

lines = [[int(y) for y in x.strip().split(' ')] for x in open("input.txt", "r").readlines()]
print((Calc(lines), Calc([x[::-1] for x in lines])))
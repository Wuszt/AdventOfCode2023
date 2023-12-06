import math
file = open("input.txt", "r")
ts = [int(x) for x in file.readline().strip().split(' ')[1:] if x != '']
ds = [int(x) for x in file.readline().strip().split(' ')[1:] if x != '']

def Calc(times, distances):
    result = 1
    for i in range(len(times)):
        delta = times[i] * times[i] - 4*(distances[i] + 1)
        x1 = (-times[i] - math.sqrt(delta)) / 2
        x2 = (-times[i] + math.sqrt(delta)) / 2
        result *= int(abs(x1)) - math.ceil(abs(x2)) + 1
    print(result)

def Multiply(someList):
    result = ''
    for s in someList: result += str(s)
    return int(result)

Calc(ts, ds)
Calc([Multiply(ts)], [Multiply(ds)])
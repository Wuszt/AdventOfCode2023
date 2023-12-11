#file = open("input.txt", "r")
#dirs = [0 if x == 'L' else 1 for x in file.readline().strip()]
#file.readline()
#places = {}
#for l in [x.strip() for x in file]:
#    place = [x.replace(',', '').replace('(', '').replace(')', '').replace('=', '').replace(' ', '') for x in l]
#    place = [x for x in place if x != '']
#    places[''.join(place[0:3])] = (''.join(place[3:6]), ''.join(place[6:9]))

#currPlace = places['AAA']
#finished = False
#result = 0
#while(True):
#    for dir in dirs:
#        result += 1
#        if currPlace[dir] == 'ZZZ':
#            finished = True
#            break
#        currPlace = places[currPlace[dir]]
#    if finished:
#        break
#print(result)

import math


file = open("input.txt", "r")
dirs = [0 if x == 'L' else 1 for x in file.readline().strip()]
file.readline()
places = {}
for l in [x.strip() for x in file]:
    place = [x.replace(',', '').replace('(', '').replace(')', '').replace('=', '').replace(' ', '') for x in l]
    place = [x for x in place if x != '']
    places[''.join(place[0:3])] = (''.join(place[3:6]), ''.join(place[6:9]))

starts = []
for place in places.keys():
    if place[-1] == 'A':
        starts.append(place)

ends = []
for place in places.keys():
    if place[-1] == 'Z':
        ends.append([place,[]])

#finished = False
#result = 0
#while(True):
#    for dir in dirs:
#        result += 1
#        finished = 0
#        for c, currPlace in enumerate(currPlaces):
#            if currPlace[dir][-1] == 'Z':
#                finished += 1
#            currPlaces[c] = places[currPlace[dir]]
#        if finished == len(currPlaces):
#            print(result)
#            exit()

finished = False
for e, end in enumerate(ends):
    its = 0
    place = places[end[0]]
    found = False
    while(not found):
        for dd in range(len(dirs)):
            ddd = its % len(dirs)
            its += 1
            if place[dirs[ddd]][-1] == 'Z':
                ends[e][1].append([ddd + 1, its])
                found = True
                break
            place = places[place[dirs[ddd]]]

basics = []

for place in starts:
    its = 0
    found = False
    while(not found):
        for dir in dirs:
            its += 1
            place = places[place][dir]
            if place[-1] == 'Z':
                basics.append([place, its])
                found = True
                break
currs = basics
#its = 0
#for c, curr in enumerate(currs):
#    its = max(its, curr[1])
#while(True):
#    for c, curr in enumerate(currs):
#        endIndex = -1
#        for e, end in enumerate(ends):
#            if end[0] == curr[0]:
#                endIndex = e
#                break

#        if curr[1] < its:
#            #offset = (ends[endIndex][1][0][0] + len(dirs) - curr[1]) % len(dirs)
#            #currs[c][1] += offset
#            cycle = ends[endIndex][1][0][1]
#            #mult = math.ceil((its - currs[c][1]) / cycle)
#            currs[c] = [ends[endIndex][0], curr[1] + cycle]
#            its = max(its, currs[c][1])
#    allDone = True
#    for curr in currs:
#        allDone &= curr[1] == its
#    if allDone:
#        print(its)
#        break

its = 0

for c, curr in enumerate(currs):
    its = max(its, curr[1])

def Iterate(left, right):
    for e, end in enumerate(ends):
            if end[0] == currs[right][0]:
                endIndex = e
                break

    cycle = ends[endIndex][1][0][1]
    mult = math.ceil((currs[left][1] - currs[right][1]) / cycle)
    currs[right] = [ends[endIndex][0], currs[right][1] + cycle * mult]
while(True):
    for i in range(1, len(currs)):
        while(True):
            left  = 0
            right = i
            if currs[left][1] == currs[right][1]:
                break
            if currs[left][1] < currs[right][1]:
                tmp = left
                left = right
                right = tmp
            Iterate(left, right)
    allDone = True
    for curr in currs[1:]:
        allDone &= currs[0][1] == curr[1]
    if allDone:
        print(currs[0][1])
        break

for c, curr in enumerate(currs):
    its = max(its, curr[1])
while(True):
    for c, curr in enumerate(currs):
        endIndex = -1
        for e, end in enumerate(ends):
            if end[0] == curr[0]:
                endIndex = e
                break

        if curr[1] < its:
            #offset = (ends[endIndex][1][0][0] + len(dirs) - curr[1]) % len(dirs)
            #currs[c][1] += offset
            cycle = ends[endIndex][1][0][1]
            #mult = math.ceil((its - currs[c][1]) / cycle)
            currs[c] = [ends[endIndex][0], curr[1] + cycle]
            its = max(its, currs[c][1])
    allDone = True
    for curr in currs:
        allDone &= curr[1] == its
    if allDone:
        print(its)
        break

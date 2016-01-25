#!/usr/bin/env python

import sys
from collections import defaultdict

def splitter(arr):
    res = []
    part = []
    cnt = 0
    for i in arr:
        if not part or i == (part[-1] + 1):
            part.append(i)
        else:
            cnt += 1
            res.append(part)
            part = [i]

    if part:
        cnt += 1
        res.append(part)
    return res, cnt

def highSec(grid):
    grid = [list(g) for g in grid]

    dots = []
    guards = 0
    gridDict = {}
    for i in range(len(grid)):
        gDict = defaultdict(list)
        indices = []
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                indices.append(j)
        dot= splitter(indices)
        dots.append(dot[0])
        guards += dot[1]
        for ditem in dot[0]:
            for d in ditem:
                gDict[d].append(len(ditem))
                gDict[d].append(ditem)
        gridDict[i] = gDict

    unavailable = [[True]*len(grid[0]) for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
                if grid[i][j] == 'X':
                    unavailable[i][j] = False

    len1 = gridDict[0]
    len2 = gridDict[1]

    for k, v in len1.iteritems():
        if v[0] == 1 and unavailable[0][k]== True and unavailable[1][k] == True:
            unavailable[1][k] = False
            guards -= 1
            unavailables = len2[k][1]
            for u in unavailables:
                unavailable[1][u] = False

    for k, v in len2.iteritems():
        if v[0] == 1 and unavailable[1][k] == True and unavailable[0][k] == True:
            unavailable[0][k] = False
            guards -= 1
            unavailables = len1[k][1]
            for u in unavailables:
                unavailable[0][u] = False

    return guards


f = open(sys.argv[1], 'r')
num = f.readline().strip()
for i in xrange(1, int(num)+1):
    n = int(f.readline().strip())
    grids = []
    for j in range(2):
        grids.append(f.readline().strip())
    guardCnt = highSec(grids)
    print "Case #%s: %s" % (i, guardCnt)

#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from collections import defaultdict
import itertools
import math

def distance(pt1, pt2):
    x_s = [pt1[0], pt2[0]]
    y_s = [pt1[1], pt2[1]]
    return (x_s[1]-x_s[0])**2+(y_s[1]-y_s[0])**2

def boomerang(stars):
    count = 0
    for star in stars:
        candidates = [s for s in stars if s != star]
        distances = defaultdict(list)
        for candidate in candidates:
            dist = distance(star, candidate)
            val = [star, candidate]
            distances[dist].append(val)
        for k, v in distances.iteritems():
            if len(v) > 1:
                combo = itertools.combinations(v, 2)
                for c in combo:
                    count += 1
    return count

f = open(sys.argv[1], 'r')
num = f.readline().strip()
for i in xrange(1, int(num)+1):
    n = int(f.readline().strip())
    stars = []
    for j in range(n):
        stars.append(map(int, f.readline().strip().split()))
    boomerangs = boomerang(stars)
    print "Case #%s: %s" % (i, boomerangs)

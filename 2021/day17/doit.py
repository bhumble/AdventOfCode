#!/usr/bin/python3

import re
import math

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

def fire(v, t):
    x = y = 0
    ymax = 0
    while x <= t[1] and y >= t[2]:
        x += v[0]
        y += v[1]
        v[0] = v[0] - 1 if v[0] > 0 else v[0] + 1 if v[0] < 0 else 0
        v[1] = v[1] - 1
        ymax = max(ymax, y)
        #print('x: ' + str(x) + ', y: ' + str(y) + ', vx: ' + str(v[0]) + ', vy: ' + str(v[1]))
        if x >= t[0] and x <= t[1] and y >= t[2] and y <= t[3]:
            return (True, ymax)
    return (False, ymax)

def part1(data):
    target = []
    for line in data:
        matches = re.search('target area: x=(-?[0-9]*)..(-?[0-9]*), y=(-?[0-9]*)..(-?[0-9]*)', line.strip())
        if matches:
            target = [int(matches.group(1)), int(matches.group(2)), int(matches.group(3)), int(matches.group(4))]

    best_ymax = 0
    for vx in range(100):
        for vy in range(100):
            (hit, ymax) = fire([vx, vy], target)
            #print((hit, ymax))
            if hit:
                best_ymax = max(ymax, best_ymax)
    return best_ymax

def part2(data):
    target = []
    for line in data:
        matches = re.search('target area: x=(-?[0-9]*)..(-?[0-9]*), y=(-?[0-9]*)..(-?[0-9]*)', line.strip())
        if matches:
            target = [int(matches.group(1)), int(matches.group(2)), int(matches.group(3)), int(matches.group(4))]

    num_hits = 0
    for vx in range(-200, 200):
        for vy in range(-200, 200):
            (hit, ymax) = fire([vx, vy], target)
            #print((hit, ymax))
            if hit:
                num_hits += 1
    return num_hits

print(part1(alldata))
print(part2(alldata))

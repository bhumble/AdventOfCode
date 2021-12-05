#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

def part1(data):
    vents = {}
    for line in data:
        matches = re.search('([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)', line.strip())
        x1 = int(matches.group(1))
        y1 = int(matches.group(2))
        x2 = int(matches.group(3))
        y2 = int(matches.group(4))
        if (x1 == x2 or y1 == y2):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    key = str(x) + ',' + str(y)
                    if key in vents:
                        vents[key] += 1
                    else:
                        vents[key] = 1

    num_overlaps = 0
    for key in vents:
        if vents[key] > 1:
            num_overlaps += 1
    return num_overlaps

def part2(data):
    vents = {}
    for line in data:
        matches = re.search('([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)', line.strip())
        x1 = int(matches.group(1))
        y1 = int(matches.group(2))
        x2 = int(matches.group(3))
        y2 = int(matches.group(4))
        if (x1 == x2 or y1 == y2):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    key = str(x) + ',' + str(y)
                    if key in vents:
                        vents[key] += 1
                    else:
                        vents[key] = 1
        else:
            #print(line.strip())
            x = x1
            y = y1
            while (x >= min(x1,x2) and x <= max(x1,x2) and y >= min(y1,y2) and y <= max(y1,y2)):
                key = str(x) + ',' + str(y)
                #print(key)
                if key in vents:
                    vents[key] += 1
                else:
                    vents[key] = 1
                if x2 > x1:
                    x += 1
                else:
                    x -= 1
                if y2 > y1:
                    y += 1
                else:
                    y -= 1

    num_overlaps = 0
    for key in vents:
        if vents[key] > 1:
            num_overlaps += 1
    return num_overlaps

print(part1(alldata))
print(part2(alldata))
#!/usr/bin/python3

import re
import math

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

def part1(data):
    # Read heightmap
    heightmap = []
    risk_sum = 0
    for line in data:
        heightmap.append([int(char) for char in line.strip()])

    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            height = heightmap[row][col]
            is_lowpoint = True
            if row > 0 and heightmap[row - 1][col] <= height: # top
                is_lowpoint = False
            if row < (len(heightmap) - 1) and heightmap[row + 1][col] <= height: # bottom
                is_lowpoint = False
            if col > 0 and heightmap[row][col - 1] <= height: # left
                is_lowpoint = False
            if col < (len(heightmap[row]) - 1) and heightmap[row][col + 1] <= height: # right
                is_lowpoint = False
            if is_lowpoint:
                #print("row: " + str(row) + ", col: " + str(col) + ", height: " + str(height))
                risk_sum += 1 + height
    return risk_sum

def get_basin(heightmap, row, col):
    height = heightmap[row][col]
    #print("basin --> row: " + str(row) + ", col: " + str(col) + ", height: " + str(height))
    basin = {}
    basin[str(row) + ',' + str(col)] = 1
    if row > 0 and heightmap[row - 1][col] != 9 and heightmap[row - 1][col] > height: # top
        basin.update(get_basin(heightmap, row - 1, col))
    if row < (len(heightmap) - 1) and heightmap[row + 1][col] != 9 and heightmap[row + 1][col] > height: # bottom
        basin.update(get_basin(heightmap, row + 1, col))
    if col > 0 and heightmap[row][col - 1] != 9 and heightmap[row][col - 1] > height: # left
        basin.update(get_basin(heightmap, row, col - 1))
    if col < (len(heightmap[row]) - 1) and heightmap[row][col + 1] != 9 and heightmap[row][col + 1] > height: # right
        basin.update(get_basin(heightmap, row, col + 1))
    return basin

def part2(data):
    # Read heightmap
    heightmap = []
    risk_sum = 0
    for line in data:
        heightmap.append([int(char) for char in line.strip()])

    basin_sizes = []

    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            height = heightmap[row][col]
            is_lowpoint = True
            if row > 0 and heightmap[row - 1][col] <= height: # top
                is_lowpoint = False
            if row < (len(heightmap) - 1) and heightmap[row + 1][col] <= height: # bottom
                is_lowpoint = False
            if col > 0 and heightmap[row][col - 1] <= height: # left
                is_lowpoint = False
            if col < (len(heightmap[row]) - 1) and heightmap[row][col + 1] <= height: # right
                is_lowpoint = False
            if is_lowpoint:
                #print("low point --> row: " + str(row) + ", col: " + str(col) + ", height: " + str(height))
                basin_sizes.append(sum(get_basin(heightmap, row, col).values()))
    return math.prod(sorted(basin_sizes)[-3:])

print(part1(alldata))
print(part2(alldata))
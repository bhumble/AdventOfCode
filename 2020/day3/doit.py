#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    data = f.readlines()
    f.close()

def part1():
    trees_hit = 0
    col = 0
    row = 1
    for line in data:
        if line[col] == "#":
            trees_hit += 1
        #print("row:{:d}, col:{:d}, tile:{:s}".format(row, col + 1, line[col]))
        col = (col + 3) % (len(line) - 1)
        row += 1
    print("{:d}".format(trees_hit))

def count_hit_trees(slope_x, slope_y):
    trees_hit = 0
    col = 0
    row = 0
    for line in data:
        if (row % slope_y) == 1:
            row += 1
            continue
        if line[col] == "#":
            trees_hit += 1
        #print("row:{:d}, col:{:d}, tile:{:s}".format(row, col + 1, line[col]))
        col = (col + slope_x) % (len(line) - 1)
        row += 1
    return trees_hit

def part2():
    print("{:d}".format(count_hit_trees(1, 1) * count_hit_trees(3, 1) * count_hit_trees(5, 1) * count_hit_trees(7, 1) * count_hit_trees(1, 2)))

part1()
part2()

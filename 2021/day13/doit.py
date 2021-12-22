#!/usr/bin/python3

import re
import math

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

def fold_left(dots, fold_pos_x):
    #print('fold left')
    to_add = []
    for y in dots.keys():
        for x in dots[y].keys():
            if x > fold_pos_x and dots[y][x] == 1:
                dots[y][x] = 0
                to_add.append([y, fold_pos_x - (x - fold_pos_x)])
    for dot in to_add:
        y = dot[0]
        x = dot[1]
        if y not in dots:
            dots[y] = {}
        dots[y][x] = 1

def fold_up(dots, fold_pos_y):
    #print('fold up')
    to_add = []
    for y in dots.keys():
        for x in dots[y].keys():
            if y > fold_pos_y and dots[y][x] == 1:
                dots[y][x] = 0
                to_add.append([fold_pos_y - (y - fold_pos_y), x])
    for dot in to_add:
        y = dot[0]
        x = dot[1]
        if y not in dots:
            dots[y] = {}
        dots[y][x] = 1

def sum_dots(dots):
    sum = 0
    for y in dots.keys():
        for x in dots[y].keys():
            sum += dots[y][x]
    return sum

def draw_dots(dots):
    min_x = 999999
    max_x = -999999
    min_y = 999999
    max_y = -999999
    for y in dots.keys():
        for x in dots[y].keys():
            if dots[y][x] == 1:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)
    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            if y in dots and x in dots[y] and dots[y][x] == 1:
                line += '#'
            else:
                line += '.'
        print(line)
    print('')

def part1(data):
    num_folds = 0
    dots = {}
    for line in data:
        if 'fold along x=' in line:
            if num_folds > 0:
                break
            [fold, x] = line.strip().split('=')
            fold_left(dots, int(x))
            num_folds += 1
            #print(sum_dots(dots))
        elif 'fold along y=' in line:
            if num_folds > 0:
                break
            [fold, y] = line.strip().split('=')
            fold_up(dots, int(y))
            num_folds += 1
            #print(sum_dots(dots))
        elif line.strip():
            [x, y] = line.strip().split(',')
            if int(y) not in dots:
                dots[int(y)] = {}
            dots[int(y)][int(x)] = 1
    return sum_dots(dots)

def part2(data):
    dots = {}
    for line in data:
        if 'fold along x=' in line:
            [fold, x] = line.strip().split('=')
            fold_left(dots, int(x))
            #draw_dots(dots)
        elif 'fold along y=' in line:
            [fold, y] = line.strip().split('=')
            fold_up(dots, int(y))
            #draw_dots(dots)
        elif line.strip():
            [x, y] = line.strip().split(',')
            if int(y) not in dots:
                dots[int(y)] = {}
            dots[int(y)][int(x)] = 1
    draw_dots(dots)
    return ''

print(part1(alldata))
print(part2(alldata))
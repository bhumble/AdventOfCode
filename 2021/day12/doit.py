#!/usr/bin/python3

import re
import math

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

num_paths = 0

def find_paths(caves, current_path):
    global num_paths
    #print(current_path)
    for path in caves[current_path[-1]]:
        #print(str(current_path) + ' --> ' + path)
        new_path = current_path.copy() + [path]
        if path == 'end':
            num_paths += 1
            #print(new_path)
        elif path.isupper() or path not in current_path:
            find_paths(caves, new_path)

def part1(data):
    global num_paths
    caves = {}
    for line in data:
        [a, b] = line.strip().split('-')
        if a not in caves:
            caves[a] = []
        if b not in caves:
            caves[b] = []
        caves[a].append(b)
        caves[b].append(a)

    #print(caves)
    num_paths = 0
    current_path = ['start']
    find_paths(caves, current_path.copy())
    return num_paths

def is_valid_path(caves, path):
    small_double_visits = 0
    if path.count('start') > 1:
        return False
    if path.count('end') > 1:
        return False
    for cave in caves:
        if cave.islower():
            if path.count(cave) > 2:
                return False
            elif path.count(cave) == 2:
                small_double_visits += 1
    return small_double_visits <= 1

def find_paths2(caves, current_path):
    global num_paths
    #print(current_path)
    for path in caves[current_path[-1]]:
        #print(str(current_path) + ' --> ' + path)
        new_path = current_path.copy() + [path]
        if path == 'end':
            num_paths += 1
            #print(new_path)
        elif is_valid_path(caves, new_path):
            find_paths2(caves, new_path)

def part2(data):
    global num_paths
    caves = {}
    for line in data:
        [a, b] = line.strip().split('-')
        if a not in caves:
            caves[a] = []
        if b not in caves:
            caves[b] = []
        caves[a].append(b)
        caves[b].append(a)

    #print(caves)
    num_paths = 0
    current_path = ['start']
    find_paths2(caves, current_path.copy())
    return num_paths

print(part1(alldata))
print(part2(alldata))
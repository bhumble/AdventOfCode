#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    data = f.readlines()
    f.close()

def part1():
    position = 0
    depth = 0
    for line in data:
        matches = re.search('([^ ]*) ([0-9]*)', line.strip())
        command = matches.group(1)
        distance = int(matches.group(2))
        if command == 'up':
            depth -= distance
        elif command == 'down':
            depth += distance
        elif command == 'forward':
            position += distance
    print(position * depth)

def part2():
    position = 0
    depth = 0
    aim = 0
    for line in data:
        matches = re.search('([^ ]*) ([0-9]*)', line.strip())
        command = matches.group(1)
        distance = int(matches.group(2))
        if command == 'up':
            aim -= distance
        elif command == 'down':
            aim += distance
        elif command == 'forward':
            position += distance
            depth += aim*distance
    print(position * depth)

part1()
part2()
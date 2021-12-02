#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    data = f.readlines()
    f.close()

data_pattern = r'([0-9]*)-([0-9]*) (.): (.*)'

def part1():
    valid_passwords = 0
    for line in data:
        matches = re.match(data_pattern, line)
        min = int(matches.group(1))
        max = int(matches.group(2))
        letter = matches.group(3)
        password = matches.group(4)
        count = password.count(letter)
        if count >= min and count <= max:
            valid_passwords += 1
    print(valid_passwords)

def part2():
    valid_passwords = 0
    for line in data:
        matches = re.match(data_pattern, line)
        pos1 = int(matches.group(1))
        pos2 = int(matches.group(2))
        letter = matches.group(3)
        password = matches.group(4)
        match1 = password[pos1 - 1] == letter
        match2 = password[pos2 - 1] == letter
        if (match1 or match2) and (match1 != match2):
            valid_passwords += 1
    print(valid_passwords)

part1()
part2()

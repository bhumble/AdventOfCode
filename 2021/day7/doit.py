#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

def part1(data):
    for line in data:
        crab_array = [int(item) for item in line.strip().split(',')]
    all_crabs = {}
    for crab in crab_array:
        if crab in all_crabs:
            all_crabs[crab] += 1
        else:
            all_crabs[crab] = 1
    min_pos = min(all_crabs.keys())
    max_pos = max(all_crabs.keys())
    fuels = []
    for rendezvous_pos in range(min_pos, max_pos+1):
        fuel = 0
        for pos in all_crabs.keys():
            fuel += all_crabs[pos] * abs(pos - rendezvous_pos)
        fuels.append(fuel)
    return min(fuels)

def part2(data):
    for line in data:
        crab_array = [int(item) for item in line.strip().split(',')]
    all_crabs = {}
    for crab in crab_array:
        if crab in all_crabs:
            all_crabs[crab] += 1
        else:
            all_crabs[crab] = 1
    min_pos = min(all_crabs.keys())
    max_pos = max(all_crabs.keys())
    fuels = []
    for rendezvous_pos in range(min_pos, max_pos+1):
        fuel = 0
        for pos in all_crabs.keys():
            fuel += all_crabs[pos] * sum(range(abs(pos - rendezvous_pos) + 1))
        fuels.append(fuel)
    return min(fuels)

print(part1(alldata))
print(part2(alldata))
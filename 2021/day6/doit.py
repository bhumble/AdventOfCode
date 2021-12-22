#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

def part1(data):
    for line in data:
        lanternfish = [int(item) for item in line.strip().split(',')]
    for day in range(80):
        for fishIdx in range(len(lanternfish)):
            if lanternfish[fishIdx] == 0:
                lanternfish.append(8)
                lanternfish[fishIdx] = 6
            else:
                lanternfish[fishIdx] -= 1
    return len(lanternfish)

def part2(data):
    for line in data:
        initfish = [int(item) for item in line.strip().split(',')]
    lanternfish = {}
    for age in range(9):
        lanternfish[age] = 0
    for age in initfish:
        lanternfish[age] += 1
    for day in range(256):
        breeding_fish = lanternfish[0]
        for age in range(8):
            lanternfish[age] = lanternfish[age + 1]
        lanternfish[6] += breeding_fish
        lanternfish[8] = breeding_fish
        #print(lanternfish)
        #print("After " + str(day) + " days, there are " + str(sum(lanternfish.values())) + " lanternfish.")
    return sum(lanternfish.values())

print(part1(alldata))
print(part2(alldata))
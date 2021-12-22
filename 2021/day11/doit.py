#!/usr/bin/python3

import re
import math

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

flash_count = 0

def flash(energy_levels, row, col):
    global flash_count
    flash_count += 1
    energy_levels[row][col] = 0
    #print('Flashing row: ' + str(row) + ', col: ' + str(col))
    #print(energy_levels)
    for rowMod in range(-1, 2, 1):
        for colMod in range(-1, 2, 1):
            if (row + rowMod) >= 0 and (row + rowMod) < len(energy_levels) and (col + colMod) >= 0 and (col + colMod) < len(energy_levels[row]) and (rowMod != 0 or colMod != 0) and energy_levels[row + rowMod][col + colMod] != 0:
                energy_levels[row + rowMod][col + colMod] += 1
                if energy_levels[row + rowMod][col + colMod] > 9:
                    flash(energy_levels, row + rowMod, col + colMod)

def step(energy_levels):
    # Charge
    for row in range(len(energy_levels)):
        for col in range(len(energy_levels[row])):
            energy_levels[row][col] += 1

    # Flash
    for row in range(len(energy_levels)):
        for col in range(len(energy_levels[row])):
            if energy_levels[row][col] > 9:
                flash(energy_levels, row, col)

def part1(data):
    global flash_count
    flash_count = 0
    energy_levels = []
    for line in data:
        row = []
        for val in line.strip():
            row.append(int(val))
        energy_levels.append(row)
    for i in range(100):
        step(energy_levels)
    return flash_count

def part2(data):
    global flash_count
    flash_count = 0
    energy_levels = []
    for line in data:
        row = []
        for val in line.strip():
            row.append(int(val))
        energy_levels.append(row)
    for i in range(1000):
        step(energy_levels)
        all_flashing = True
        for row in range(len(energy_levels)):
            for col in range(len(energy_levels[row])):
                if energy_levels[row][col] != 0:
                    all_flashing = False
        if all_flashing:
            return i+1
    return 0

print(part1(alldata))
print(part2(alldata))
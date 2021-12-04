#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

def part1(data):
    zeroes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in data:
        for bit in range(len(line.strip())):
            if line[bit] == '0':
                zeroes[bit] += 1;
            elif line[bit] == '1':
                ones[bit] += 1;
    gamma_bits = ''
    epsilon_bits = ''
    for bit in range(12):
        if (ones[bit] > zeroes[bit]):
            gamma_bits += '1'
            epsilon_bits += '0'
        elif (ones[bit] < zeroes[bit]):
            gamma_bits += '0'
            epsilon_bits += '1'
    gamma = int(gamma_bits, 2)
    epsilon = int(epsilon_bits, 2)
    print(gamma * epsilon)

def part2_oxygen(data, filter):
    zeroes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bit_pos = len(filter)
    match_count = 0
    match = 0
    for line in data:
        if line[0:bit_pos] == filter:
            match_count += 1
            match = line
            for bit in range(len(line.strip())):
                if line[bit] == '0':
                    zeroes[bit] += 1;
                elif line[bit] == '1':
                    ones[bit] += 1;
    #print('match_count: ', match_count)
    if match_count == 1:
        #print('match: ', match.strip())
        return int(match.strip(), 2)
    if ones[bit_pos] >= zeroes[bit_pos]:
        filter += '1';
    elif ones[bit_pos] < zeroes[bit_pos]:
        filter += '0';
    #print('filter: ', filter)
    return part2_oxygen(data, filter)

def part2_co2(data, filter):
    zeroes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bit_pos = len(filter)
    match_count = 0
    match = 0
    for line in data:
        if line[0:bit_pos] == filter:
            match_count += 1
            match = line
            for bit in range(len(line.strip())):
                if line[bit] == '0':
                    zeroes[bit] += 1;
                elif line[bit] == '1':
                    ones[bit] += 1;
    #print('match_count: ', match_count)
    if match_count == 1:
        #print('match: ', match.strip())
        return int(match.strip(), 2)
    if ones[bit_pos] < zeroes[bit_pos]:
        filter += '1';
    elif ones[bit_pos] >= zeroes[bit_pos]:
        filter += '0';
    #print('filter: ', filter)
    return part2_co2(data, filter)

def part2(data):
    oxygen = part2_oxygen(data, '')
    co2 = part2_co2(data, '')
    #print('oxygen: ', oxygen)
    #print('co2: ', co2)
    print(oxygen * co2)

part1(alldata)
part2(alldata)
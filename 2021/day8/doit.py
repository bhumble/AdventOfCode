#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

def part1(data):
    total_1_4_7_8 = 0
    for line in data:
        cols = line.strip().split(' | ')
        patterns = cols[0].strip().split(' ')
        outputs = cols[1].strip().split(' ')
        for output in outputs:
            if len(output) == 2: # 1
                total_1_4_7_8 += 1
            elif len(output) == 4: # 4
                total_1_4_7_8 += 1
            elif len(output) == 3: # 7
                total_1_4_7_8 += 1
            elif len(output) == 7: # 8
                total_1_4_7_8 += 1
    return total_1_4_7_8

def fanout(word):
    return sorted([char for char in word])

def read_7seg(wires):
    code = ''.join(str(wire) for wire in wires)
    if code == 'abcefg':
        return 0
    elif code == 'cf':
        return 1
    elif code == 'acdeg':
        return 2
    elif code == 'acdfg':
        return 3
    elif code == 'bcdf':
        return 4
    elif code == 'abdfg':
        return 5
    elif code == 'abdefg':
        return 6
    elif code == 'acf':
        return 7
    elif code == 'abcdefg':
        return 8
    elif code == 'abcdfg':
        return 9
    return -1

def write_7seg(number):
    if number == 0:
        return fanout('abcefg')
    elif number == 1:
        return fanout('cf')
    elif number == 2:
        return fanout('acdeg')
    elif number == 3:
        return fanout('acdfg')
    elif number == 4:
        return fanout('bcdf')
    elif number == 5:
        return fanout('abdfg')
    elif number == 6:
        return fanout('abdefg')
    elif number == 7:
        return fanout('acf')
    elif number == 8:
        return fanout('abcdefg')
    elif number == 9:
        return fanout('abcdfg')
    return []

def is_valid_7seg(wires):
    return read_7seg(wires) >= 0

def remap_wires(wirein, wiremap):
    wireout = []
    for wire in wirein:
        wireout.append(wiremap[wire])
    return sorted(wireout)

def get_wiremap(patterns):
        # Initialize wire map
        abcdefg = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        wiremap = {}
        for wire in abcdefg:
            wiremap[wire] = abcdefg.copy()

        # Determine wire mappings
        for pattern in patterns:
            if len(pattern) == 2: # 1
                for wirein in fanout(pattern):
                    for wireout in abcdefg:
                        if wireout not in write_7seg(1):
                            if wireout in wiremap[wirein]:
                                wiremap[wirein].remove(wireout)
                for wirein in abcdefg:
                    if wirein not in fanout(pattern):
                        for wireout in write_7seg(1):
                            if wireout in wiremap[wirein]:
                                wiremap[wirein].remove(wireout)
            elif len(pattern) == 4: # 4
                for wirein in fanout(pattern):
                    for wireout in abcdefg:
                        if wireout not in write_7seg(4):
                            if wireout in wiremap[wirein]:
                                wiremap[wirein].remove(wireout)
                for wirein in abcdefg:
                    if wirein not in fanout(pattern):
                        for wireout in write_7seg(4):
                            if wireout in wiremap[wirein]:
                                wiremap[wirein].remove(wireout)
            elif len(pattern) == 3: # 7
                for wirein in fanout(pattern):
                    for wireout in abcdefg:
                        if wireout not in write_7seg(7):
                            if wireout in wiremap[wirein]:
                                wiremap[wirein].remove(wireout)
                for wirein in abcdefg:
                    if wirein not in fanout(pattern):
                        for wireout in write_7seg(7):
                            if wireout in wiremap[wirein]:
                                wiremap[wirein].remove(wireout)
        for a_to in wiremap['a']:
            for b_to in wiremap['b']:
                for c_to in wiremap['c']:
                    for d_to in wiremap['d']:
                        for e_to in wiremap['e']:
                            for f_to in wiremap['f']:
                                for g_to in wiremap['g']:
                                    candidate_map = {'a': a_to, 'b': b_to, 'c': c_to, 'd': d_to, 'e': e_to, 'f': f_to, 'g': g_to}
                                    is_valid = True
                                    for pattern in patterns:
                                        is_valid &= is_valid_7seg(remap_wires(pattern, candidate_map))
                                    if is_valid:
                                        return candidate_map

def part2(data):
    total = 0
    for line in data:
        # Parse notes
        cols = line.strip().split(' | ')
        patterns = cols[0].strip().split(' ')
        outputs = cols[1].strip().split(' ')
        wiremap = get_wiremap(patterns)
        decoded_output = ''
        for output in outputs:
            decoded_output += str(read_7seg(remap_wires(fanout(output), wiremap)))
        total += int(decoded_output)
    return total

print(part1(alldata))
print(part2(alldata))
#!/usr/bin/python3

import re
import math

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

def step(polymer_template, pair_insertion_rules):
    result = polymer_template[0]
    prev_char = ''
    for i in range(len(polymer_template)):
        if i > 0:
            pair = prev_char + polymer_template[i]
            if pair in pair_insertion_rules:
                result += pair_insertion_rules[pair] + polymer_template[i]
            else:
                result += polymer_template[i]
        prev_char = polymer_template[i]
    return result

def part1(data):
    polymer_template = ''
    pair_insertion_rules = {}
    for line in data:
        if not polymer_template:
            polymer_template = line.strip()
        elif line.strip():
            [a, b] = line.strip().split(' -> ')
            pair_insertion_rules[a] = b
    #print(polymer_template)
    #print(pair_insertion_rules)

    # repeat 10 times
    result = polymer_template
    for i in range(10):
        result = step(result, pair_insertion_rules)
    #print(result)

    element_counts = {}
    for element in result:
        element_counts[element] = result.count(element)
    sorted_element_counts = sorted(element_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_element_counts[0][1] - sorted_element_counts[-1][1]

def step2(pairs, pair_insertion_rules):
    result = {}
    for pair in pairs.keys():
        count = pairs[pair]
        if pair in pair_insertion_rules:
            new_pair_1 = pair[0] + pair_insertion_rules[pair]
            new_pair_2 = pair_insertion_rules[pair] + pair[1]
            if new_pair_1 in result:
                result[new_pair_1] += count
            else:
                result[new_pair_1] = count
            if new_pair_2 in result:
                result[new_pair_2] += count
            else:
                result[new_pair_2] = count
        else:
            if pair in result:
                result[pair] += count
            else:
                result[pair] = count
    return result

def part2(data):
    polymer_template = ''
    pair_insertion_rules = {}
    for line in data:
        if not polymer_template:
            polymer_template = line.strip()
        elif line.strip():
            [a, b] = line.strip().split(' -> ')
            pair_insertion_rules[a] = b
    #print(polymer_template)
    #print(pair_insertion_rules)

    # extract pairs:
    pairs = {}
    prev_char = ''
    for i in range(len(polymer_template)):
        if i > 0:
            pair = prev_char + polymer_template[i]
            if pair in pairs:
                pairs[pair] += 1
            else:
                pairs[pair] = 1
        prev_char = polymer_template[i]
    #print(pairs)

    # repeat 40 times
    result = pairs
    for i in range(40):
        result = step2(result, pair_insertion_rules)
        #print(result)

    element_counts = {}
    for pair in result.keys():
        count = result[pair]
        if pair[0] in element_counts:
            element_counts[pair[0]] += count
        else:
            element_counts[pair[0]] = count
        if pair[1] in element_counts:
            element_counts[pair[1]] += count
        else:
            element_counts[pair[1]] = count
    sorted_element_counts = sorted(element_counts.items(), key=lambda x: x[1], reverse=True)
    #print(sorted_element_counts)
    return math.floor((sorted_element_counts[0][1] - sorted_element_counts[-1][1]) / 2) # FIXME: why /2 ??? Where am I double-counting???

print(part1(alldata))
print(part2(alldata))
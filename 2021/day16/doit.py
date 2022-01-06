#!/usr/bin/python3

import re
import math

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

version_sum = 0

def parse_literal(payload, offset):
    value_bin = ''
    keep_going = '1'
    while keep_going == '1':
        keep_going = payload[offset]
        offset += 1
        value_bin += payload[offset:offset+4]
        offset += 4
    value = int(value_bin, 2)
    #print('literal: ' + str(value))
    return (offset, value)

def parse(payload, offset):
    global version_sum
    #print('parsing @ ' + str(offset))
    version = int(payload[offset:offset+3], 2)
    offset += 3
    type_id = int(payload[offset:offset+3], 2)
    offset += 3
    #print('version: ' + str(version) + ', type_id: ' + str(type_id))
    version_sum += version
    result = 0
    values = []
    if type_id == 4: # literal
        (offset, result) = parse_literal(payload, offset)
    else: # operator
        length_type_id = payload[offset]
        offset += 1
        #print('operator: length_type_id: ' + str(length_type_id))
        if length_type_id == '0':
            length = int(payload[offset:offset+15], 2)
            offset += 15
            #print('length: ' + str(length))
            end = offset + length
            while offset < end:
                (offset, value) = parse(payload, offset)
                values.append(value)
            #print('end operator')
        elif length_type_id == '1':
            num_packets = int(payload[offset:offset+11], 2)
            offset += 11
            #print('num_packets: ' + str(num_packets))
            for packet in range(num_packets):
                (offset, value) = parse(payload, offset)
                values.append(value)
            #print('end operator')

        # Apply operators to values
        #print('type_id: ' + str(type_id) + ', values: ' + str(values))
        if type_id == 0:
            result = sum(values)
        elif type_id == 1:
            result = math.prod(values)
        elif type_id == 2:
            result = min(values)
        elif type_id == 3:
            result = max(values)
        elif type_id == 5:
            result = 1 if (values[0] > values[1]) else 0
        elif type_id == 6:
            result = 1 if (values[0] < values[1]) else 0
        elif type_id == 7:
            result = 1 if (values[0] == values[1]) else 0
    return (offset, result)

def part1(data):
    payload = ''
    for line in data:
        payload += bin(int(line.strip(), 16))[2:]
    while len(payload) % 4 != 0:
        payload = '0' + payload
    #print(payload)

    offset = 0
    parse(payload, offset)
    return version_sum

def part2(data):
    payload = ''
    for line in data:
        payload += bin(int(line.strip(), 16))[2:]
    while len(payload) % 4 != 0:
        payload = '0' + payload
    #print(payload)

    offset = 0
    (offset, value) = parse(payload, offset)
    return value

print(part1(alldata))
print(part2(alldata))

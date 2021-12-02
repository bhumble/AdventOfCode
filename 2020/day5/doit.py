#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    data = f.readlines()
    f.close()

def part1():
    highest_seat_id = 0
    for line in data:
        binary = line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0");
        row = (int(binary[0]) << 6) + (int(binary[1]) << 5) + (int(binary[2]) << 4) + (int(binary[3]) << 3) + (int(binary[4]) << 2) + (int(binary[5]) << 1) + int(binary[6]);
        col = (int(binary[7]) << 2) + (int(binary[8]) << 1) + int(binary[9]);
        seat_id = row * 8 + col
        if seat_id > highest_seat_id:
            #print("row:{:d}, col:{:d}".format(row, col))
            highest_seat_id = seat_id
    print(highest_seat_id)

def part2():
    all_seat_ids = []
    for line in data:
        binary = line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0");
        row = (int(binary[0]) << 6) + (int(binary[1]) << 5) + (int(binary[2]) << 4) + (int(binary[3]) << 3) + (int(binary[4]) << 2) + (int(binary[5]) << 1) + int(binary[6]);
        col = (int(binary[7]) << 2) + (int(binary[8]) << 1) + int(binary[9]);
        seat_id = row * 8 + col
        all_seat_ids.append(seat_id)
    all_seat_ids.sort()
    i = 0
    while i < len(all_seat_ids):
        a = all_seat_ids[i - 1]
        b = all_seat_ids[i]
        if (i >= 1) and ((b - a) > 1):
            #print("a:{:d}, b:{:d}".format(a, b))
            print(a + 1)
        i += 1

part1()
part2()
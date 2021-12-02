#!/usr/bin/python3

with open('input.txt', 'r') as f:
    data = f.readlines()
    f.close()

def part1():
    for n1 in data:
        for n2 in data:
            if (int(n1) + int(n2) == 2020):
                print(int(n1) * int(n2))
                return

def part2():
    for n1 in data:
        for n2 in data:
            for n3 in data:
                if (int(n1) + int(n2) + int(n3) == 2020):
                    print(int(n1) * int(n2) * int(n3))
                    return

part1()
part2()

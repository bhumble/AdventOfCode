#!/usr/bin/python3

from collections import deque

with open('input.txt', 'r') as f:
    data = f.readlines()
    f.close()

def part1():
    # Count how many times the number got larger than the previous entry
    i = 0
    answer = 0
    prevValue = 0
    for line in data:
        value = int(line.strip())
        if (i > 0 and value > prevValue):
            answer += 1
            #print(value, " (increased)")
        #else:
            #print(value)
        i += 1
        prevValue = value
    print(answer)

def part2():
    # Count how many times the sum of a 3-sample window got larger than the previous window
    i = 0
    answer = 0
    window = deque([0, 0, 0])
    for line in data:
        value = int(line.strip())
        popped = window.popleft()
        if (i > 2 and (sum(window) + value) > (popped + sum(window))):
            answer += 1
            window.append(value)
            #print(window, " (increased)")
        else:
            window.append(value)
            #print(window)
        i += 1
    print(answer)

part1()
part2()
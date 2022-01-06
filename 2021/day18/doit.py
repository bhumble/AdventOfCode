#!/usr/bin/python3

import re
import math

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

def explode(num):
    depth = 0
    for i in range(len(num)):
        if num[i] == '[':
            depth += 1
        elif num[i] == ']':
            depth -= 1

        if i >= 2 and depth > 4 and num[i].isdigit() and num[i-1] == ',' and num[i-2].isdigit():
            left_val = int(num[i-2])
            right_val = int(num[i])

            # Explode left
            for j in range(i-3, -1, -1):
                if num[j].isdigit():
                    num[j] = str(int(num[j]) + left_val)
                    break

            # Explode right
            for j in range(i+1, len(num)):
                if num[j].isdigit():
                    num[j] = str(int(num[j]) + right_val)
                    break

            num.pop(i-3) # [
            num.pop(i-3) # leftNum
            num.pop(i-3) # ,
            num.pop(i-3) # rightNum
            num.pop(i-3) # ]
            num.insert(i-3, '0')

            #print('after expode :  ' + ''.join(num))
            return (True, num)

    # Nothing to do, just return original number
    return (False, num)

def split(num):
    for i in range(len(num)):
        if num[i].isdigit() and int(num[i]) >= 10:
            val = int(num[i])
            num.pop(i)
            num.insert(i, ']')
            num.insert(i, str(math.ceil(val/2.0)))
            num.insert(i, ',')
            num.insert(i, str(math.floor(val/2.0)))
            num.insert(i, '[')

            #print('after split:  ' + ''.join(num))
            return (True, num)

    # Nothing to do, just return original number
    return (False, num)

def reduce(num):
    (changed, num) = explode(num)
    while changed:
        (changed, num) = explode(num)
        if not changed:
            (changed, num) = split(num)
    return num

def magnitude(num):
    if isinstance(num, list) and len(num) == 2:
        return 3 * magnitude(num[0]) + 2 * magnitude(num[1])
    else:
        return num

def part1(data):
    sum = []
    for line in data:
        num = [x for x in line.strip()]
        reduced = reduce(num)
        if not sum:
            sum = reduced
            continue
        sum = ['['] + sum + [','] + reduced + [']']
        #print('after addition: ' + ''.join(sum))
        sum = reduce(sum)
    return magnitude(eval(''.join(sum)))

def part2(data):
    largest_magnitude = 0
    for line1 in data:
        num1 = reduce([x for x in line1.strip()])
        for line2 in data:
            num2 = reduce([x for x in line2.strip()])
            sum = ['['] + num1 + [','] + num2 + [']']
            sum = reduce(sum)
            mag = magnitude(eval(''.join(sum)))
            largest_magnitude = max(largest_magnitude, mag)
    return largest_magnitude

print(part1(alldata))
print(part2(alldata))

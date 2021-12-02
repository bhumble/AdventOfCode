#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    data = f.readlines()
    f.close()
    data.append("\n")

def part1():
    num_yeses = 0
    answers = {}
    for line in data:
        if line.isspace(): # new group
            #print(len(answers))
            #print(answers)
            num_yeses += len(answers)
            answers = {}
        else:
            for char in line:
                if char.isalpha():
                    answers[char] = 1
    num_yeses += len(answers)
    print(num_yeses)

def part2():
    total_num_yeses = 0
    num_people_in_party = 0
    answers = {}
    for line in data:
        if line.isspace(): # new group
            num_yeses_in_party = 0
            #print(answers)
            for i in answers:
                if answers[i] == num_people_in_party:
                    num_yeses_in_party += 1
            #print(num_yeses_in_party)
            answers = {}
            num_people_in_party = 0
            total_num_yeses += num_yeses_in_party
        else:
            for char in line:
                if char.isalpha():
                    if char in answers:
                        answers[char] += 1
                    else:
                        answers[char] = 1
            num_people_in_party += 1
    print(total_num_yeses)

part1()
part2()
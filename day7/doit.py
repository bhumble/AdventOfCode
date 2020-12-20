#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    data = f.readlines()
    f.close()
    data.append("\n")


# Parse rules
rules = {}
for line in data:
    matches = re.match(r'(.*) bags contain (.*)', line)
    if not matches:
        continue
    holder = matches.group(1)
    heldBags = matches.group(2).split(", ")
    if holder not in rules:
        rules[holder] = []
    for rule in heldBags:
        if rule == "no other bags.":
            continue
        matches = re.match(r'([0-9]*) (.*) bag.*', rule)
        count = int(matches.group(1))
        heldBag = matches.group(2)
        for i in range(count):
            rules[holder].append(heldBag)
        #print(rules)

canHoldShinyGoldBag = []

def whatCanHold(innerBag):
    for outerBag in rules:
        if innerBag in rules[outerBag]:
            canHoldShinyGoldBag.append(outerBag)
            whatCanHold(outerBag)

shinyGoldBagHolds = []

def heldBy(outerBag):
    for innerBag in rules[outerBag]:
        shinyGoldBagHolds.append(innerBag)
        heldBy(innerBag)

def part1():
    # Count how many bags can directly or evenutally hold my "shiny gold" bag
    whatCanHold("shiny gold")
    dedup = list(set(canHoldShinyGoldBag))
    print(len(dedup))

def part2():
    # Count how many bags can be directly or evenutally held by my "shiny gold" bag
    heldBy("shiny gold")
    print(len(shinyGoldBagHolds))

part1()
part2()
#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    data = f.readlines()
    f.close()

def part1():
    valid_passports = 0
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    for line in data:
        if line.isspace():
            byr = False
            iyr = False
            eyr = False
            hgt = False
            hcl = False
            ecl = False
            pid = False
            #print("RESET")
        else:
            byr |= "byr:" in line
            iyr |= "iyr:" in line
            eyr |= "eyr:" in line
            hgt |= "hgt:" in line
            hcl |= "hcl:" in line
            ecl |= "ecl:" in line
            pid |= "pid:" in line

            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                valid_passports += 1
                byr = False
                iyr = False
                eyr = False
                hgt = False
                hcl = False
                ecl = False
                pid = False

        #print("{:s} --> {:d}".format(line, valid_passports))
    print(valid_passports)

def part2():
    valid_passports = 0
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    for line in data:
        if line.isspace():
            byr = False
            iyr = False
            eyr = False
            hgt = False
            hcl = False
            ecl = False
            pid = False
            #print("RESET")
        else:
            _byr = -1
            matches = re.match(r'.*byr:([0-9]{4})\s', line)
            if matches:
                _byr = int(matches.group(1))
                byr |= _byr >= 1920 and _byr <= 2002

            _iyr = -1
            matches = re.match(r'.*iyr:([0-9]{4})\s', line)
            if matches:
                _iyr = int(matches.group(1))
                iyr |= _iyr >= 2010 and _iyr <= 2020

            _eyr = -1
            matches = re.match(r'.*eyr:([0-9]{4})\s', line)
            if matches:
                _eyr = int(matches.group(1))
                eyr |= _eyr >= 2020 and _eyr <= 2030

            _hgt = -1
            matches = re.match(r'.*hgt:([0-9]*)cm\s', line)
            if matches:
                _hgt = int(matches.group(1))
                hgt |= _hgt >= 150 and _hgt <= 193
            matches = re.match(r'.*hgt:([0-9]*)in\s', line)
            if matches:
                _hgt = int(matches.group(1))
                hgt |= _hgt >= 59 and _hgt <= 76

            hcl |= not not re.match(r'.*hcl:#[0-9a-f]{6}[^0-9a-f]', line)

            _ecl = ""
            matches = re.match(r'.*ecl:([a-z]{3})\s', line)
            if matches:
                _ecl = matches.group(1)
                ecl |= _ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

            pid |= not not re.match(r'.*pid:[0-9]{9}[^0-9]', line)

            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                valid_passports += 1
                byr = False
                iyr = False
                eyr = False
                hgt = False
                hcl = False
                ecl = False
                pid = False

        #print("{:s} --> {:d}".format(line, valid_passports))
    print(valid_passports)

part1()
part2()

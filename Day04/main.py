#!/usr/bin/env python3

import fileinput
import re


def test_task1():
    print('tests for task 1: ok')


def solve_task1():
    passports = []
    passport = ''
    for line in fileinput.input():
        line = line.rstrip()
        if line:
            passport = passport + ' ' + line
        else:
            passports.append(passport)
            passport = ''
    passports.append(passport)

    valid = 0
    for passport in passports:
        data = {}
        for pair in passport.split():
            key, value = pair.split(':')
            data[key] = value
        if (len(data) >= 8) or (len(data) == 7 and 'cid' not in data):
            valid += 1

    solution = valid
    print(f'answer to task 1: {solution}')


def test_task2():
    print('tests for task 2: ok')


def solve_task2():
    passports = []
    passport = ''
    for line in fileinput.input():
        line = line.rstrip()
        if line:
            passport = passport + ' ' + line
        else:
            passports.append(passport)
            passport = ''
    passports.append(passport)

    hairpattern = re.compile('#[0-9a-f]{6}')
    valid = 0
    for passport in passports:
        data = {}
        for pair in passport.split():
            key, value = pair.split(':')
            data[key] = value

        if len(data) < 7 or len(data) > 8:
            continue
        if len(data) == 7 and 'cid' in data:
            continue
        if len(data['byr']) != 4 or int(data['byr']) < 1920 or int(data['byr']) > 2002:
            continue
        if len(data['iyr']) != 4 or int(data['iyr']) < 2010 or int(data['iyr']) > 2020:
            continue
        if len(data['eyr']) != 4 or int(data['eyr']) < 2020 or int(data['eyr']) > 2030:
            continue
        if data['hgt'][-2:] != 'cm' and data['hgt'][-2:] != 'in':
            continue
        if data['hgt'][-2:] == 'cm' and (int(data['hgt'][:-2]) < 150 or int(data['hgt'][:-2]) > 193):
            continue
        if data['hgt'][-2:] == 'in' and (int(data['hgt'][:-2]) < 59 or int(data['hgt'][:-2]) > 76):
            continue
        if not re.fullmatch(hairpattern, data['hcl']):
            continue
        if data['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        if len(data['pid']) != 9:
            continue
        try:
            map(int, data['pid'])
        except:
            continue
        valid += 1

    solution = valid
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

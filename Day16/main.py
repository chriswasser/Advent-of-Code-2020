#!/usr/bin/env python3

import fileinput
import re
import numpy as np
from collections import defaultdict

def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    rules = lines[:lines.index('')]
    tickets = lines[lines.index('nearby tickets:') + 1:]
    
    rule_pattern = r'.*: (\d+)-(\d+) or (\d+)-(\d+)'
    allowed = set()
    for rule in rules:
        match = re.fullmatch(rule_pattern, rule)
        for i in range(int(match.group(1)), int(match.group(2)) + 1):
            allowed.add(i)
        for i in range(int(match.group(3)), int(match.group(4)) + 1):
            allowed.add(i)
    
    error = 0
    for ticket in tickets:
        values = list(map(int, ticket.split(',')))
        for value in values:
            if value not in allowed:
                error += value

    solution = error
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    rules = lines[:lines.index('')]
    myticket = lines[lines.index('your ticket:') + 1]
    tickets = lines[lines.index('nearby tickets:') + 1:]
    
    rule_pattern = r'(.*): (\d+)-(\d+) or (\d+)-(\d+)'
    allowed = set()
    for rule in rules:
        match = re.fullmatch(rule_pattern, rule)
        for i in range(int(match.group(2)), int(match.group(3)) + 1):
            allowed.add(i)
        for i in range(int(match.group(4)), int(match.group(5)) + 1):
            allowed.add(i)
    
    valid = []
    for ticket in tickets:
        values = list(map(int, ticket.split(',')))
        for value in values:
            if value not in allowed:
                break
        else:
            valid.append(values)
    
    matrix = np.array(valid)
    mapping = defaultdict(list)
    for rule in rules:
        match = re.fullmatch(rule_pattern, rule)
        allowed = set()
        for i in range(int(match.group(2)), int(match.group(3)) + 1):
            allowed.add(i)
        for i in range(int(match.group(4)), int(match.group(5)) + 1):
            allowed.add(i)

        for column in range(matrix.shape[1]):
            for value in matrix[:, column]:
                if value not in allowed:
                    break
            else:
                mapping[match.group(1)].append(column)

    fixed = {}
    while True:
        for key, value in mapping.items():
            if len(value) == 1:
                fixed[key] = value[0]
                break
        del mapping[key]
        for k, v in mapping.items():
            if fixed[key] in v:
                v.remove(fixed[key])
        if not mapping:
            break
    
    myticket = list(map(int, myticket.split(',')))
    product = 1
    for key, value in fixed.items():
        if key[:9] == 'departure':
            product *= myticket[value]

    solution = product
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

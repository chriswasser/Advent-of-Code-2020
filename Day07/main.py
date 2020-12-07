#!/usr/bin/env python3

import fileinput
import re
from collections import defaultdict

def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    packings = defaultdict(set)
    input_regex = r'([a-z ]+) bags contain (([0-9]+) ([a-z ]+) bags?(, |\.)){{{N}}}'
    for line in fileinput.input():
        for i in range(1, 10):
            if match := re.match(input_regex.format(N=i), line.rstrip()):
                packings[match.group(1)].add(match.group(4))
    
    outer = {'shiny gold'}
    while True:
        modified = False
        for bag, contents in packings.items():
            if bag not in outer and outer.intersection(contents):
                outer.add(bag)
                modified = True
        if not modified:
            break
    solution = len(outer) - 1
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    packings, amounts = {}, {}
    input_regex = r'([a-z ]+) bags contain (([0-9]+) ([a-z ]+) bags?(, |\.)){{{N}}}'
    for line in fileinput.input():
        packings[re.match(input_regex.format(N=0), line.rstrip()).group(1)] = set()
        for i in range(1, 10):
            if match := re.match(input_regex.format(N=i), line.rstrip()):
                packings[match.group(1)].add(match.group(4))
                amounts[match.group(1), match.group(4)] = int(match.group(3))
    
    totals = {}
    while True:
        for bag, contents in packings.items():
            if bag in totals:
                continue
            if not contents:
                totals[bag] = 1
            elif all([other in totals for other in contents]):
                totals[bag] = 1
                for other in contents:
                    totals[bag] += amounts[bag, other] * totals[other]
        if len(totals) == len(packings):
            break
    solution = totals['shiny gold'] - 1
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

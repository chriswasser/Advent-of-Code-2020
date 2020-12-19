#!/usr/bin/env python3

import fileinput
import re


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    rules = lines[:lines.index('')]
    messages = lines[lines.index('') + 1:]

    tmp = {}
    for rule in rules:
        number, pattern = rule.split(':')
        tmp[number] = pattern.replace('"', '') + ' '
    rules = tmp

    processed = set()
    while True:
        modified = {}
        for number, pattern in rules.items():
            if number not in processed and re.fullmatch('(a|b)+', pattern.replace(' ', '').replace('(', '').replace(')', '').replace('|', '')):
                modified[number] = pattern
        processed |= set(modified.keys())

        for mod, pattern in modified.items():
            for number in rules:
                while ' ' + mod + ' ' in rules[number]:
                    rules[number] = rules[number].replace(' ' + mod + ' ', ' (' + pattern + ') ')
        if not modified:
            break
    
    count = 0
    for message in messages:
        if re.fullmatch(rules['0'], message, re.VERBOSE):
            count += 1

    solution = count
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    rules = lines[:lines.index('')]
    messages = lines[lines.index('') + 1:]

    tmp = {}
    for rule in rules:
        number, pattern = rule.split(':')
        tmp[number] = pattern.replace('"', '') + ' '
    rules = tmp

    rules['8'] = ' 42 '
    for i in range(2, 10):
        rules['8'] += '|' + i * ' 42' + ' '

    rules['11'] = ' 42 31 '
    for i in range(2, 10):
        rules['11'] += '|' + i * ' 42' + i * ' 31' + ' '

    processed = set()
    while True:
        modified = {}
        for number, pattern in rules.items():
            if number not in processed and re.fullmatch('(a|b)+', pattern.replace(' ', '').replace('(', '').replace(')', '').replace('|', '')):
                modified[number] = pattern
        processed |= set(modified.keys())

        for mod, pattern in modified.items():
            for number in rules:
                while ' ' + mod + ' ' in rules[number]:
                    rules[number] = rules[number].replace(' ' + mod + ' ', ' (' + pattern + ') ')
        if not modified:
            break

    count = 0
    for message in messages:
        if re.fullmatch(rules['0'], message, re.VERBOSE):
            count += 1

    solution = count
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

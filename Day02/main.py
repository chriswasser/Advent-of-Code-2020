#!/usr/bin/env python3

import fileinput


def test_task1():
    print('tests for task 1: ok')


def solve_task1():
    valid = 0
    for line in fileinput.input():
        range_, char, password = line.rstrip().replace(':', '').split()
        low, high = map(int, range_.split('-'))
        amount = password.count(char)
        if low <= amount and amount <= high:
            valid += 1
    solution = valid
    print(f'answer to task 1: {solution}')


def test_task2():
    print('tests for task 2: ok')


def solve_task2():
    valid = 0
    for line in fileinput.input():
        range_, char, password = line.rstrip().replace(':', '').split()
        first, second = map(int, range_.split('-'))
        if (password[first - 1] == char and not password[second - 1] == char) or \
            (not password[first - 1] == char and password[second - 1] == char):
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

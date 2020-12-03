#!/usr/bin/env python3

import fileinput


def test_task1():
    print('tests for task 1: ok')


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    num_columns = len(lines[0])
    column, counter = 0, 0
    for row, line in enumerate(lines):
        if row == 0:
            continue
        column = (column + 3) % num_columns
        if line[column] == '#':
            counter += 1
    solution = counter
    print(f'answer to task 1: {solution}')


def test_task2():
    print('tests for task 2: ok')


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    num_columns = len(lines[0])
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    product = 1
    for slope in slopes:
        row, column, counter = 0, 0, 0
        while row + slope[1] < len(lines):
            row = row + slope[1]
            column = (column + slope[0]) % num_columns
            if lines[row][column] == '#':
                counter += 1
        product *= counter
    solution = product
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

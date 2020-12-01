#!/usr/bin/env python3

import fileinput


def find_sum2(numbers, target):
    for ia, a in enumerate(numbers):
        for b in numbers[ia + 1:]:
            if a + b == target:
                return a, b


def find_sum3(numbers, target):
    for ia, a in enumerate(numbers):
        for ib, b in enumerate(numbers[ia + 1:]):
            for c in numbers[ia + 1:][ib + 1:]:
                if a + b + c == target:
                    return a, b, c


def test_task1():
    expenses = [1721, 979, 366, 299, 675, 1456]
    a, b = find_sum2(expenses, 2020)
    assert a * b == 514579
    print('tests for task 1: ok')


def solve_task1():
    expenses = [int(line) for line in fileinput.input()]
    a, b = find_sum2(expenses, 2020)
    solution = a * b
    print(f'answer to task 1: {solution}')


def test_task2():
    expenses = [1721, 979, 366, 299, 675, 1456]
    a, b, c = find_sum3(expenses, 2020)
    assert a * b * c == 241861950
    print('tests for task 2: ok')


def solve_task2():
    expenses = [int(line) for line in fileinput.input()]
    a, b, c = find_sum3(expenses, 2020)
    solution = a * b * c
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import fileinput
from collections import Counter


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    numbers = sorted(int(line.rstrip()) for line in fileinput.input())
    numbers = [0] + numbers + [max(numbers) + 3]
    diffs = Counter(b - a for a, b in zip(numbers[:-1], numbers[1:]))
    solution = diffs[1] * diffs[3]
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    numbers = sorted(int(line.rstrip()) for line in fileinput.input())
    numbers = [0] + numbers + [max(numbers) + 3]
    diffs = [b - a for a, b in zip(numbers[:-1], numbers[1:])]

    counters = []
    counter = 0
    for diff in diffs:
        if diff == 1:
            counter += 1
        else:
            counters.append(counter)
            counter = 0
    counters.append(counter)

    factors = {
        0: 1,
        1: 1,
        2: 2,
        3: 4,
        4: 7,
    }
    num_configurations = 1
    for counter in counters:
        num_configurations *= factors[counter]


    solution = num_configurations
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

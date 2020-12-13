#!/usr/bin/env python3

import fileinput
import numpy as np


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    with fileinput.input() as file:
        time = int(next(file).rstrip())
        busses = np.array(list(map(int, filter(lambda bus: bus != 'x', next(file).rstrip().split(',')))))
    for i in range(1000):
        modulos = (time + i) % busses == 0
        if np.any(modulos):
            solution = i * busses[modulos][0]
            break
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    with fileinput.input() as file:
        time = int(next(file).rstrip())
        busses = [(offset, int(schedule))
                  for offset, schedule in enumerate(next(file).rstrip().split(',')) if schedule != 'x']

    # assume schedules are coprime
    # --> apply chinese remainder theorem (see: https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
    M = 1
    for offset, schedule in busses:
        M *= schedule

    x = 0
    for offset, schedule in busses:
        gcd, r, s = egcd(schedule, int(M / schedule))
        e = s * int(M / schedule)
        x += -1 * offset * e

    solution = x % M
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

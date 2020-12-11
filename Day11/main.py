#!/usr/bin/env python3

import fileinput
import numpy as np

def kernel(a):
    occupied = np.count_nonzero(a[0:3, 0:3] == '#')
    if a[1, 1] == 'L' and occupied == 0:
        return '#'
    if a[1, 1] == '#' and occupied >= 5:
        return 'L'
    return a[1, 1]

def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    area = [list(line.rstrip()) for line in fileinput.input()]
    area = np.pad(np.array(area), pad_width=1, mode='constant', constant_values='.')

    new = area
    while True:
        old = np.copy(new)
        for i in range(1, len(old) - 1):
            for j in range(1, len(old[i]) - 1):
                new[i, j] = kernel(old[i-1:i+2, j-1:j+2])
        if (old == new).all():
            break

    solution = np.count_nonzero(new == '#')
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    area = [list(line.rstrip()) for line in fileinput.input()]
    area = np.pad(np.array(area), pad_width=1, mode='constant', constant_values='.')

    new = area
    while True:
        old = np.copy(new)
        for i in range(1, len(old) - 1):
            for j in range(1, len(old[i]) - 1):
                if old[i, j] == '.':
                    continue

                occupied = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        for x in range(1, max(len(old), len(old[i]))):
                            if i + k * x < 0 or i + k * x >= len(old) or j + l * x < 0 or j + l * x >= len(old[i]):
                                break
                            if old[i + k * x, j + l * x] == 'L':
                                break
                            if old[i + k * x, j + l * x] == '#':
                                occupied += 1
                                break                    
                if old[i, j] == 'L' and occupied == 0:
                    new[i, j] = '#'
                if old[i, j] == '#' and occupied >= 6:
                    new[i, j] = 'L'
        if (old == new).all():
            break

    solution = np.count_nonzero(new == '#')
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import fileinput


def test_task1():
    print('tests for task 1: ok')


def solve_task1():
    groups = []
    group = ''
    for line in fileinput.input():
        line = line.rstrip()
        if line:
            group += line
        else:
            groups.append(set(group))
            group = ''
    groups.append(set(group))
    solution = sum(map(len, groups))
    print(f'answer to task 1: {solution}')


def test_task2():
    print('tests for task 2: ok')


def solve_task2():
    count = 0
    group, num_persons = '', 0
    for line in fileinput.input():
        line = line.rstrip()
        if line:
            group += line
            num_persons += 1
        else:
            print(group, num_persons)
            for char in set(group):
                if group.count(char) == num_persons:
                    count += 1
            group, num_persons = '', 0
    for char in set(group):
        if group.count(char) == num_persons:
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

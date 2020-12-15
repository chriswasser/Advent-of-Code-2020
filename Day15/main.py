#!/usr/bin/env python3

from collections import defaultdict
import fileinput


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    start = list(map(int, lines[0].split(',')))

    numbers, occurrences = [], defaultdict(list)
    for index, number in enumerate(start):
        numbers.append(number)
        occurrences[number].append(index)
    for turn in range(len(numbers), 2020):
        number = numbers[-1]
        new = 0 if len(occurrences[number]) < 2 else occurrences[number][-1] - occurrences[number][-2]
        numbers.append(new)
        occurrences[new].append(turn)
    
    solution = numbers[2020 - 1]
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    start = list(map(int, lines[0].split(',')))

    numbers, occurrences = [], defaultdict(list)
    for index, number in enumerate(start):
        numbers.append(number)
        occurrences[number].append(index)
    for turn in range(len(numbers), 30000000):
        number = numbers[-1]
        new = 0 if len(occurrences[number]) < 2 else occurrences[number][-1] - occurrences[number][-2]
        numbers.append(new)
        occurrences[new].append(turn)
    
    solution = numbers[30000000 - 1]
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import fileinput
import math


def find_sum(numbers, num_summands, target):
    if num_summands == 0 and target == 0:
        return True, []
    if num_summands == 0 or target < 0 or len(numbers) == 0:
        return False, None
    for index, number in enumerate(numbers):
        found_solution, summands = find_sum(numbers[index+1:], num_summands - 1, target - number)
        if found_solution:
            return True, summands + [number]
    return False, None


def test_task1():
    expenses = [1721, 979, 366, 299, 675, 1456]
    found_solution, summands = find_sum(expenses, 2, 2020)
    assert found_solution
    assert math.prod(summands) == 514579
    print('tests for task 1: ok')


def solve_task1():
    expenses = [int(line) for line in fileinput.input()]
    found_solution, summands = find_sum(expenses, 2, 2020)
    assert found_solution
    solution = math.prod(summands)
    print(f'answer to task 1: {solution}')


def test_task2():
    expenses = [1721, 979, 366, 299, 675, 1456]
    found_solution, summands = find_sum(expenses, 3, 2020)
    assert found_solution
    assert math.prod(summands) == 241861950
    print('tests for task 2: ok')


def solve_task2():
    expenses = [int(line) for line in fileinput.input()]
    found_solution, summands = find_sum(expenses, 3, 2020)
    assert found_solution
    solution = math.prod(summands)
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

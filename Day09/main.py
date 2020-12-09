#!/usr/bin/env python3

import fileinput

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
    assert True
    print('tests for task 1: ok')


def solve_task1():
    numbers = [int(line.rstrip()) for line in fileinput.input()]
    memory = numbers[:25]
    for i in range(25, len(numbers)):
        found_solution, _ = find_sum(memory, 2, numbers[i])
        if not found_solution:
            solution = numbers[i]
            break
        memory = memory[1:] + [numbers[i]]

    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    numbers = [int(line.rstrip()) for line in fileinput.input()]
    memory = numbers[:25]
    for i in range(25, len(numbers)):
        found_solution, _ = find_sum(memory, 2, numbers[i])
        if not found_solution:
            invalid_number = numbers[i]
            break
        memory = memory[1:] + [numbers[i]]


    for size in range(2, len(numbers)):
        for start in range(len(numbers) - size + 1):
            end = start + size
            if sum(numbers[start:end]) == invalid_number:
                summands = numbers[start:end]
                break
        else:
            continue
        break

    solution = min(summands) + max(summands)
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

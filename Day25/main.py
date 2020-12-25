#!/usr/bin/env python3

import fileinput


def transform(value, subject_number=7):
    return (value * subject_number) % 20201227


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    card_public_key = int(lines[0])
    door_public_key = int(lines[1])

    value, loop_size = 1, 0
    while True:
        loop_size += 1
        value = transform(value, subject_number=7)
        if value == card_public_key:
            card_loop_size = loop_size
            break
    
    value = 1
    for _ in range(card_loop_size):
        value = transform(value, subject_number=door_public_key)
    encryption_key = value

    solution = encryption_key
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    solution = None
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

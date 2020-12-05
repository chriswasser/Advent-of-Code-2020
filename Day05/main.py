#!/usr/bin/env python3

import fileinput


def test_task1():
    print('tests for task 1: ok')


def solve_task1():
    seats = []
    for line in fileinput.input():
        line = line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        seats.append(int(line, base=2))
    solution = max(seats)
    print(f'answer to task 1: {solution}')


def test_task2():
    print('tests for task 2: ok')


def solve_task2():
    seats = []
    for line in fileinput.input():
        line = line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        seats.append(int(line, base=2))
    seats.sort()
    last = seats[0]
    for seat in seats[1:]:
        if seat == last + 1:
            last = seat
        else:
            solution = last + 1
            break
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

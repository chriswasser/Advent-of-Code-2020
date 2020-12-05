#!/usr/bin/env python3

import fileinput


def seat_from_ticket(ticket):
    return int(ticket.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), base=2)


def find_missing_seat(seats):
    seats = sorted(seats)
    for seat1, seat2 in zip(seats[:-1], seats[1:]):
        if seat1 + 1 != seat2:
            return seat1 + 1


def test_task1():
    assert seat_from_ticket('FBFBBFFRLR') == 357
    assert seat_from_ticket('BFFFBBFRRR') == 567
    assert seat_from_ticket('FFFBBBFRRR') == 119
    assert seat_from_ticket('BBFFBBFRLL') == 820
    print('tests for task 1: ok')


def solve_task1():
    seats = [seat_from_ticket(line.rstrip()) for line in fileinput.input()]
    solution = max(seats)
    print(f'answer to task 1: {solution}')


def test_task2():
    print('tests for task 2: ok')


def solve_task2():
    seats = [seat_from_ticket(line.rstrip()) for line in fileinput.input()]
    solution = find_missing_seat(seats)
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

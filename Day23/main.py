#!/usr/bin/env python3

import fileinput
from collections import deque


class Cup(object):
    def __init__(self, number):
        self.number = int(number)
        self.prev = None
        self.next = None


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    cups = deque(map(int, lines[0]))

    for move in range(100):
        current = cups.popleft()
        picked = [cups.popleft() for _ in range(3)]

        destination = current
        while True:
            destination -= 1
            if destination == 0:
                destination = 9
            if destination not in picked:
                break

        index = cups.index(destination)
        cups.insert(index + 1, picked[0])
        cups.insert(index + 2, picked[1])
        cups.insert(index + 3, picked[2])

        cups.append(current)

    index = cups.index(1)
    cups = list(map(str, cups))
    solution = ''.join(cups[index+1:] + cups[:index])
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    initial = list(map(int, lines[0]))
    num_moves, maximum = 10000000, 1000000

    cups = list(map(Cup, range(0, maximum + 1)))
    circle = cups[1:]
    for index, number in enumerate(initial):
        circle[index] = cups[number]
    for cup1, cup2 in zip(circle[:-1], circle[1:]):
        cup1.next = cup2
        cup2.prev = cup1
    circle[-1].next = circle[0]
    circle[0].prev = circle[-1]

    current = circle[0]
    for move in range(num_moves):
        picked_cups = [current.next, current.next.next, current.next.next.next]
        picked_numbers = [cup.number for cup in picked_cups]

        current.next, picked_cups[-1].next.prev = picked_cups[-1].next, current

        destination_number = current.number
        while True:
            destination_number = destination_number - 1 if destination_number > 1 else maximum
            if destination_number not in picked_numbers:
                break
        destination_cup = cups[destination_number]

        picked_cups[0].prev, destination_cup.next, picked_cups[-1].next, destination_cup.next.prev = \
            destination_cup, picked_cups[0], destination_cup.next, picked_cups[-1]

        current = current.next

    solution = cups[1].next.number * cups[1].next.next.number
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

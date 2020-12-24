#!/usr/bin/env python3

import fileinput
from collections import Counter, defaultdict


def coordinate(directions):
    x, y = 0, 0
    for direction in directions:
        if direction == 'ne':
            x, y = x + 0.5, y + 0.5
        if direction == 'e':
            x, y = x + 1.0, y + 0.0
        if direction == 'se':
            x, y = x + 0.5, y - 0.5
        if direction == 'sw':
            x, y = x - 0.5, y - 0.5
        if direction == 'w':
            x, y = x - 1.0, y + 0.0
        if direction == 'nw':
            x, y = x - 0.5, y + 0.5
    return x, y

def count_adjacent(x, y, current):
    count = 0
    if (x + 0.5, y + 0.5) in current:
        count += 1
    if (x + 1.0, y + 0.0) in current:
        count += 1
    if (x + 0.5, y - 0.5) in current:
        count += 1
    if (x - 0.5, y - 0.5) in current:
        count += 1
    if (x - 1.0, y + 0.0) in current:
        count += 1
    if (x - 0.5, y + 0.5) in current:
        count += 1
    return count

def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    tiles = []
    for line in lines:
        directions = []
        index = 0
        while index < len(line):
            direction = line[index]
            index += 1
            if direction == 's' or direction == 'n':
                direction += line[index]
                index += 1
            directions.append(direction)
        tiles.append(directions)

    counts = defaultdict(int)
    for directions in tiles:
        counts[coordinate(directions)] += 1
    black = sum([count % 2 == 1 for coord, count in counts.items()])

    solution = black
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    tiles = []
    for line in lines:
        directions = []
        index = 0
        while index < len(line):
            direction = line[index]
            index += 1
            if direction == 's' or direction == 'n':
                direction += line[index]
                index += 1
            directions.append(direction)
        tiles.append(directions)

    counts = defaultdict(int)
    for directions in tiles:
        counts[coordinate(directions)] += 1
    black = [coord for coord, count in counts.items() if count % 2 == 1]

    current = set(black)
    for _ in range(100):
        new = set()

        # update black tiles
        for coord in current:
            count = count_adjacent(*coord, current)
            if 1 <= count and count <= 2:
                new.add(coord)

        # update white tiles
        for x, y in current:
            if count_adjacent(x + 0.5, y + 0.5, current) == 2:
                new.add((x + 0.5, y + 0.5))
            if count_adjacent(x + 1.0, y + 0.0, current) == 2:
                new.add((x + 1.0, y + 0.0))
            if count_adjacent(x + 0.5, y - 0.5, current) == 2:
                new.add((x + 0.5, y - 0.5))
            if count_adjacent(x - 0.5, y - 0.5, current) == 2:
                new.add((x - 0.5, y - 0.5))
            if count_adjacent(x - 1.0, y + 0.0, current) == 2:
                new.add((x - 1.0, y + 0.0))
            if count_adjacent(x - 0.5, y + 0.5, current) == 2:
                new.add((x - 0.5, y + 0.5))

        current = new

    solution = len(current)
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

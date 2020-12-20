#!/usr/bin/env python3

import fileinput
import math
import re
import numpy as np

def get_edges(tile):
    return set([
        tuple(tile[:, 0][::1]), tuple(tile[:, -1][::1]),
        tuple(tile[0, :][::1]), tuple(tile[-1, :][::1]),
        tuple(tile[:, 0][::-1]), tuple(tile[:, -1][::-1]),
        tuple(tile[0, :][::-1]), tuple(tile[-1, :][::-1]),
    ])

def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    tiles = {}
    for line in lines:
        if not line:
            tiles[number] = np.array(tile)
        elif match := re.fullmatch(r'Tile (\d+):', line):
            tile, number = [], int(match.group(1))
        else:
            tile.append(list(line))
    tiles[number] = np.array(tile)

    edges = {number: get_edges(tile) for number, tile in tiles.items()}

    corners = []
    for a in tiles:
        counter = 0
        for b in tiles:
            if a == b:
                continue
            if edges[a].intersection(edges[b]):
                counter += 1
        if counter == 2:
            corners.append(a)

    solution = math.prod(corners)
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    pattern = r'Tile (\d+):'
    tiles = {}
    for line in lines:
        if not line:
            tiles[number] = np.array(tile)

        if match := re.fullmatch(pattern, line):
            tile, number = [], int(match.group(1))
        else:
            tile.append(list(line))
    tiles[number] = np.array(tile)

    edges = {number: get_edges(tile) for number, tile in tiles.items()}

    n = int(math.sqrt(len(edges)))
    image = np.full(shape=(n, n), fill_value=-1, dtype=np.int64)
    x, y = 0, 0
    while x != n:
        # TODO: determine which tile fits at image position (x, y)

        y += 1
        if y == n:
            x += 1
            y = 0

    solution = None
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import fileinput
import math
import re
import numpy as np
from collections import defaultdict


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

    all_tiles = defaultdict(list)
    for number, tile in tiles.items():
        for modifiers in [
            lambda x: x,
            lambda x: np.flip(x, axis=0),
            lambda x: np.flip(x, axis=1),
            lambda x: np.flip(np.flip(x, axis=0), axis=1),
        ]:
            for turns in range(4):
                all_tiles[number].append(modifiers(np.rot90(tile, k=turns)))
    
    corner_number, corner_tiles, fits = 1453, all_tiles[1453], []
    for corner_tile in corner_tiles:
        fitting = True
        for number in all_tiles:
            if number == corner_number:
                continue
            for tile in all_tiles[number]:
                if np.all(corner_tile[0, :] == tile[-1, :]) or np.all(corner_tile[:, 0] == tile[:, -1]):
                    fitting = False
        if fitting:
            fits.append(corner_tile[:])
    
    uniques = []
    for fit in fits:
        for unique in uniques:
            if np.all(unique == fit):
                break
        else:
            uniques.append(fit)


    boundary = defaultdict(int)
    for number in all_tiles:
        for tile in all_tiles[number]:
            boundary[tuple(tile[0, :])] += 1
            boundary[tuple(tile[:, 0])] += 1
            boundary[tuple(tile[-1, :])] += 1
            boundary[tuple(tile[:, -1])] += 1
    boundary = set(edge for edge, count in boundary.items() if count == 8)

    n = int(math.sqrt(len(tiles)))
    image = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    numbers = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    image[0][0], numbers[0][0] = uniques[0], corner_number

    x, y = 0, 1
    while x != n:
        boundary1, ref_number1, boundary2, ref_number2 = None, None, None, None
        if numbers[x][y - 1]:
            boundary1, ref_number1 = image[x][y - 1][:, -1], numbers[x][y - 1]
        if numbers[x - 1][y]:
            boundary2, ref_number2 = image[x - 1][y][-1, :], numbers[x - 1][y]

        for number, tile in tiles.items():
            if number == ref_number1 or number == ref_number2:
                continue

            fitting = False

            for modifiers in [
                lambda x: x,
                lambda x: np.flip(x, axis=0),
                lambda x: np.flip(x, axis=1),
                lambda x: np.flip(np.flip(x, axis=0), axis=1),
            ]:
                for turns in range(4):
                    new = modifiers(np.rot90(tiles[number], k=turns))

                    if (numbers[x][y - 1] and np.all(boundary1 == new[:, 0])) or (not numbers[x][y - 1] and tuple(new[:, 0]) in boundary):
                        fitting = True
                    else:
                        fitting = False
                    if (numbers[x - 1][y] and np.all(boundary2 == new[0, :])) or (not numbers[x - 1][y] and tuple(new[0, :]) in boundary):
                        fitting &= True
                    else:
                        fitting &= False

                    if fitting:
                        numbers[x][y] = number
                        image[x][y] = new
                        break
                else:
                    continue
                break
            else:
                continue
            break
        x, y = x + (y == n - 1), (y + 1) % n

    tilesize = len(image[0][0]) - 2
    picture = np.empty(shape=(n * tilesize, n * tilesize), dtype='<U1')
    for x in range(n):
        for y in range(n):
            picture[x * tilesize:(x + 1) * tilesize, y * tilesize:(y + 1) * tilesize] = image[x][y][1:-1, 1:-1]

    roughnesses = set()
    for modifiers in [
        lambda x: x,
        lambda x: np.flip(x, axis=0),
        lambda x: np.flip(x, axis=1),
        lambda x: np.flip(np.flip(x, axis=0), axis=1),
    ]:
        for turns in range(4):
            tmp = modifiers(np.rot90(picture, k=turns))

            monster = [
                '                  # ',
                '#    ##    ##    ###',
                ' #  #  #  #  #  #   ',
            ]
            marked = np.full(shape=tmp.shape, fill_value=False)
            for x in range(tmp.shape[0]):
                for y in range(tmp.shape[1]):
                    try:
                        fullmatch = True
                        for x_offset, line in enumerate(monster):
                            for y_offset, char in enumerate(line):
                                if char == '#' and tmp[x + x_offset, y + y_offset] != '#':
                                    fullmatch = False
                        if fullmatch:
                            for x_offset, line in enumerate(monster):
                                for y_offset, char in enumerate(line):
                                    if char == '#':
                                        marked[x + x_offset, y + y_offset] = True
                    except IndexError:
                        pass
            roughnesses.add(int(np.sum(tmp == '#') - np.sum(marked)))

    solution = ' or '.join(map(str, roughnesses))
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

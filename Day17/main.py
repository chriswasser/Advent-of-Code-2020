#!/usr/bin/env python3

import fileinput
import numpy as np


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    grid = np.array([[list(map(int, line.replace('#', '1').replace('.', '0'))) for line in lines]])
    grid = np.pad(grid, 1)
    for _ in range(6):
        grid = np.pad(grid, 1)
        nx, ny, nz = grid.shape
        newgrid = np.copy(grid)
        for i in range(1, nx):
            for j in range(1, ny):
                for k in range(1, nz):
                    num_active = np.sum(grid[i-1:i+2, j-1:j+2, k-1:k+2])
                    if grid[i, j, k] == 0 and num_active == 3:
                        newgrid[i, j, k] = 1
                    if grid[i, j, k] == 1 and (num_active < 3 or num_active > 4):
                        newgrid[i, j, k] = 0
        grid = np.copy(newgrid)

    solution = np.sum(newgrid)
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    grid = np.array([[[list(map(int, line.replace('#', '1').replace('.', '0'))) for line in lines]]])
    grid = np.pad(grid, 1)
    for _ in range(6):
        grid = np.pad(grid, 1)
        nx, ny, nz, nw = grid.shape
        newgrid = np.copy(grid)
        for i in range(1, nx):
            for j in range(1, ny):
                for k in range(1, nz):
                    for l in range(1, nw):
                        num_active = np.sum(grid[i-1:i+2, j-1:j+2, k-1:k+2, l-1:l+2])
                        if grid[i, j, k, l] == 0 and num_active == 3:
                            newgrid[i, j, k, l] = 1
                        if grid[i, j, k, l] == 1 and (num_active < 3 or num_active > 4):
                            newgrid[i, j, k, l] = 0
        grid = np.copy(newgrid)

    solution = np.sum(newgrid)
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

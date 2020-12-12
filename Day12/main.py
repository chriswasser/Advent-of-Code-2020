#!/usr/bin/env python3

import fileinput
import numpy as np


def move(position, direction, action, argument):
    directions = [
        np.array([ 0,  1]),
        np.array([ 1,  0]),
        np.array([ 0, -1]),
        np.array([-1,  0]),
    ]
    if action == 'L':
        direction = (direction - int(argument / 90) + len(directions)) % len(directions)
    if action == 'R':
        direction = (direction + int(argument / 90) + len(directions)) % len(directions)
    if action == 'F':
        position += directions[direction] * argument
    if action == 'N':
        position += directions[0] * argument
    if action == 'E':
        position += directions[1] * argument
    if action == 'S':
        position += directions[2] * argument
    if action == 'W':
        position += directions[3] * argument

    return position, direction

def move2(ship, waypoint, action, argument):
    directions = [
        np.array([ 0,  1]),
        np.array([ 1,  0]),
        np.array([ 0, -1]),
        np.array([-1,  0]),
    ]
    if action == 'L':
        waypoint = waypoint - ship
        for _ in range(int(argument / 90)):
            waypoint[0], waypoint[1] = -1 * waypoint[1], waypoint[0]
        waypoint = waypoint + ship
    if action == 'R':
        waypoint = waypoint - ship
        for _ in range(int(argument / 90)):
            waypoint[0], waypoint[1] = waypoint[1], -1 * waypoint[0]
        waypoint = waypoint + ship
    if action == 'F':
        translation = (waypoint - ship) * argument
        ship, waypoint = ship + translation, waypoint + translation
    if action == 'N':
        waypoint = waypoint + directions[0] * argument
    if action == 'E':
        waypoint = waypoint + directions[1] * argument
    if action == 'S':
        waypoint = waypoint + directions[2] * argument
    if action == 'W':
        waypoint = waypoint + directions[3] * argument

    return ship, waypoint


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    direction, position = 1, np.array([0, 0])
    for line in fileinput.input():
        position, direction = move(position, direction, line[0], int(line[1:].rstrip()))
    solution = np.sum(np.abs(position))
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    ship, waypoint = np.array([0, 0]), np.array([10, 1])
    for line in fileinput.input():
        ship, waypoint = move2(ship, waypoint, line[0], int(line[1:].rstrip()))
    solution = np.sum(np.abs(ship))
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

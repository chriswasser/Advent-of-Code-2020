#!/usr/bin/env python3

import itertools
import fileinput
import re


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    memory = {}
    for line in lines:
        if line[:7] == 'mask = ':
            mask = line[7:]
            and_mask = int(mask.replace('X', '1'), base=2)
            or_mask = int(mask.replace('X', '0'), base=2)
        else:
            match = re.match(r'mem\[([0-9]+)\] = ([0-9]+)', line)
            memory[int(match.group(1))] = int(match.group(2)) & and_mask | or_mask
    solution = sum(memory.values())
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    memory = {}
    for line in lines:
        if line[:7] == 'mask = ':
            mask = line[7:]
        else:
            match = re.match(r'mem\[([0-9]+)\] = ([0-9]+)', line)
            address = int(match.group(1))
            value = int(match.group(2))

            pattern = ''.join([
                c2 if c1 == '0' else c1
                for c1, c2 in zip(mask, bin(address)[2:].rjust(len(mask), '0'))
            ])

            addresses = [pattern]
            for i in range(pattern.count('X')):
                addresses = [
                    address.replace('X', number, 1)
                    for address, number in itertools.product(addresses, ['0', '1'])
                ]

            for address in addresses:
                memory[int(address, base=2)] = value

    solution = sum(memory.values())
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

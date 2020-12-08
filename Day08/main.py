#!/usr/bin/env python3

import fileinput


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    program = []
    for line in fileinput.input():
        instruction, argument = line.rstrip().split()
        program.append((instruction, int(argument)))
    
    instrpointer, accumulator = 0, 0
    visited = set()
    while True:
        visited.add(instrpointer)
        instruction, argument = program[instrpointer]
        if instruction == 'nop':
            instrpointer += 1
        elif instruction == 'jmp':
            instrpointer += argument
        elif instruction == 'acc':
            accumulator += argument
            instrpointer += 1
        if instrpointer in visited:
            break
        
    solution = accumulator
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    program = []
    for line in fileinput.input():
        instruction, argument = line.rstrip().split()
        program.append((instruction, int(argument)))
    
    for linenum, line in enumerate(program):
        if line[0] == 'nop':
            modified = program[:linenum] + [('jmp', line[1])] + program[linenum+1:]
        elif line[0] == 'jmp':
            modified = program[:linenum] + [('nop', line[1])] + program[linenum+1:]
        elif line[0] == 'acc':
            modified = program[:]

        instrpointer, accumulator = 0, 0
        visited = set()
        while True:
            visited.add(instrpointer)
            if instrpointer > len(modified):
                segfault = True
                break
            if instrpointer == len(modified):
                segfault = False
                break
            instruction, argument = modified[instrpointer]
            if instruction == 'nop':
                instrpointer += 1
            elif instruction == 'jmp':
                instrpointer += argument
            elif instruction == 'acc':
                accumulator += argument
                instrpointer += 1
            if instrpointer in visited:
                segfault = True
                break
        
        if not segfault:
            break
        
    solution = accumulator
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

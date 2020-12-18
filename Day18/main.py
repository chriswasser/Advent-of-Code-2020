#!/usr/bin/env python3

import fileinput


def is_operator(token):
    return token == '+' or token == '*'


def evaluate(expression):
    # shunting yard algorithm (infix to reverse polish notation)
    output, operators = [], []
    for token in expression:
        if token.isdigit():
            output.append(token)
        elif is_operator(token):
            while operators and is_operator(operators[-1]) and operators[-1] != '(':
                output.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if operators and operators[-1] == '(':
                operators.pop()
    while operators:
        output.append(operators.pop())

    stack = []
    for token in output:
        if token.isdigit():
            stack.append(token)
        elif is_operator(token):
            a, b = stack.pop(), stack.pop()
            stack.append(str(eval(a + token + b)))
    result = int(stack.pop())

    return result


def evaluate2(expression):
    # higher precedence operator bind stronger
    precendes = {
        '+': 1,
        '*': 0,
    }

    # shunting yard algorithm (infix to reverse polish notation)
    output, operators = [], []
    for token in expression:
        if token.isdigit():
            output.append(token)
        elif is_operator(token):
            while operators and is_operator(operators[-1]) and precendes[operators[-1]] >= precendes[token] and operators[-1] != '(':
                output.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if operators and operators[-1] == '(':
                operators.pop()
    while operators:
        output.append(operators.pop())

    stack = []
    for token in output:
        if token.isdigit():
            stack.append(token)
        elif is_operator(token):
            a, b = stack.pop(), stack.pop()
            stack.append(str(eval(a + token + b)))
    result = int(stack.pop())

    return result


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    expressions = [line.rstrip().replace(' ', '') for line in fileinput.input()]

    sum_ = 0
    for expression in expressions:
        sum_ += evaluate(expression)

    solution = sum_
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    expressions = [line.rstrip().replace(' ', '') for line in fileinput.input()]

    sum_ = 0
    for expression in expressions:
        sum_ += evaluate2(expression)

    solution = sum_
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import fileinput
from collections import deque
from itertools import islice


def combat(deck1, deck2):
    while deck1 and deck2:
        player1, player2 = deck1.popleft(), deck2.popleft()
        if player1 > player2:
            deck1.append(player1)
            deck1.append(player2)
        else:
            deck2.append(player2)
            deck2.append(player1)
    return deck1 or deck2


def recursive_combat(deck1, deck2):
    memory = set()
    while deck1 and deck2:
        serialized = tuple(deck1), tuple(deck2)
        if serialized in memory:
            return deck1, 1
        memory.add(serialized)

        player1, player2 = deck1.popleft(), deck2.popleft()
        if len(deck1) >= player1 and len(deck2) >= player2:
            _, winner = recursive_combat(deque(islice(deck1, player1)), deque(islice(deck2, player2)))
        else:
            winner = 1 if player1 > player2 else 2

        if winner == 1:
            deck1.append(player1)
            deck1.append(player2)
        else:
            deck2.append(player2)
            deck2.append(player1)
    return deck1 if deck1 else deck2, 1 if deck1 else 2


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    deck1 = list(map(int, lines[1:lines.index('Player 2:') - 1]))
    deck2 = list(map(int, lines[lines.index('Player 2:') + 1:]))

    winner = combat(deque(deck1, maxlen=len(deck1) + len(deck2)), deque(deck2, maxlen=len(deck1) + len(deck2)))

    solution = sum((len(winner) - index) * card for index, card in enumerate(winner))
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    deck1 = list(map(int, lines[1:lines.index('Player 2:') - 1]))
    deck2 = list(map(int, lines[lines.index('Player 2:') + 1:]))

    deck, _ = recursive_combat(deque(deck1, maxlen=len(deck1) + len(deck2)),
                               deque(deck2, maxlen=len(deck1) + len(deck2)))

    solution = sum((len(deck) - index) * card for index, card in enumerate(deck))
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

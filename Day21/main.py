#!/usr/bin/env python3

from copy import copy
import fileinput
import re


def test_task1():
    assert True
    print('tests for task 1: ok')


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    foods, all_ingredients, all_allergens = dict(), set(), set()
    for line in lines:
        match = re.fullmatch(r'(.*) \(contains (.*)\)', line)
        ingredients, allergens = set(match.group(1).split(' ')), set(match.group(2).split(', '))

        foods[tuple(ingredients)] = allergens
        all_ingredients |= ingredients
        all_allergens |= allergens

    safe = copy(all_ingredients)
    for allergen in all_allergens:
        unsafe = set()
        for ingredients, allergens in foods.items():
            if allergen in allergens:
                if unsafe:
                    unsafe &= set(ingredients)
                else:
                    unsafe = set(ingredients)
        safe -= unsafe

    count = 0
    for ingredient in safe:
        for food in foods:
            if ingredient in food:
                count += 1

    solution = count
    print(f'answer to task 1: {solution}')


def test_task2():
    assert True
    print('tests for task 2: ok')


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    foods, all_ingredients, all_allergens = dict(), set(), set()
    for line in lines:
        match = re.fullmatch(r'(.*) \(contains (.*)\)', line)
        ingredients, allergens = set(match.group(1).split(' ')), set(match.group(2).split(', '))

        foods[tuple(ingredients)] = allergens
        all_ingredients |= ingredients
        all_allergens |= allergens

    safe = copy(all_ingredients)
    for allergen in all_allergens:
        unsafe = set()
        for ingredients, allergens in foods.items():
            if allergen in allergens:
                if unsafe:
                    unsafe &= set(ingredients)
                else:
                    unsafe = set(ingredients)
        safe -= unsafe

    unsafe = all_ingredients - safe
    mapping = {}
    for ingredient in unsafe:
        possible_allergens = copy(all_allergens)
        for food in foods:
            if ingredient not in food:
                possible_allergens -= set(foods[food])
        mapping[ingredient] = possible_allergens
    
    fixed = {}
    while True:
        for ingredient, allergens in mapping.items():
            if len(allergens) == 1:
                fixed[ingredient] = allergens.pop()
                break

        del mapping[ingredient]
        for other in mapping:
            mapping[other].discard(fixed[ingredient])

        if not mapping:
            break

    sorted_allergens = list(sorted(fixed.values()))
    sorted_ingredients = []
    for allergen in sorted_allergens:
        for ingredient in fixed:
            if fixed[ingredient] == allergen:
                sorted_ingredients.append(ingredient)
                break

    solution = ','.join(sorted_ingredients)
    print(f'answer to task 2: {solution}')


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == '__main__':
    main()

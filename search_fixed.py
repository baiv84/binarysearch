# -*- coding: utf-8 -*-
import sys
from random import sample, randint


def iterable_search(digits, target):
    """Iterable binary search function"""
    left, right = 0, len(digits) - 1
    while left <= right:
        middle = (left + right) // 2
        if digits[middle] < target:
            left = middle + 1
        elif digits[middle] > target:
            right = middle - 1
        else:
            return middle
    return


def recursive_search(digits, low, high, target):
    """Recursive binary search function"""
    if high >= low:
        mid = (high + low) // 2
        if digits[mid] == target:
            return mid
        elif digits[mid] > target:
            return recursive_search(digits, low, mid - 1, target)
        else:
            return recursive_search(digits, mid + 1, high, target)
    else:
        return


# Table of search functions
FUNC_TABLE = {
    0: iterable_search,                # Pointer to iteration search function
    1: recursive_search,               # Pointer to recursive search function
}


if __name__ == "__main__":
    # Generate random integer sorted sequence
    list_len = 10
    digits = sorted(sample(range(0, 101, 2), list_len))

    # Randomly define search mode
    rand_integer = randint(0, 99)
    func_index = rand_integer % 2
    search_func = FUNC_TABLE[func_index]

    # Run search engine
    try:
        target = int(input('Pick a number between 0-100: '))
        if (target < 0 or target > 100):
            print('Incorrect input value. Min val = 0, Max val = 100')
            sys.exit(1)

        if (func_index == 0):
            print('ITERABLE SEARCH MODE !!!')
            target_index = iterable_search(digits, target)
        else:
            print('RECURSIVE SEARCH MODE !!!')
            target_index = recursive_search(digits, 0, len(digits)-1, target)

        print(f'List: {digits}')
        if target_index is not None:
            print(f'Found {target} in index {target_index+1}')
        else:
            print(f'Cannot find {target} in the list')
    except ValueError:
        print('Invalid input')

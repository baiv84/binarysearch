# -*- coding: utf-8 -*-
from random import sample, randint


def s(list_, target):
    """Iterable binary search function"""
    left, right = 0, len(list_) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_[middle] < target:
            left = middle + 1
        elif list_[middle] > target:
            right = middle - 1
        else:
            return middle
    return


def s_recursive(arr, low, high, x):
    """Recursive binary search function"""
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return s_recursive(arr, low, mid - 1, x)
        else:
            return s_recursive(arr, mid + 1, high, x)
    else:
        return


# Table of search functions
FUNC_TABLE = {
    0: s,                # Pointer to iteration search function
    1: s_recursive,      # Pointer to recursive search function
}


if __name__ == "__main__":
    # Generate random integer sorted sequence
    list_len = 10
    rand_list = sorted(sample(range(0, 101, 2), list_len))

    # Randomly define search mode
    rand_integer = randint(0, 99)
    func_index = rand_integer % 2
    search_func = FUNC_TABLE[func_index]

    # Run search engine
    try:
        target = int(input('Pick a number between 0-100: '))
        if (func_index == 0):
            print('ITERABLE SEARCH MODE !!!')
            target_index = s(rand_list, target)
        else:
            print('RECURSIVE SEARCH MODE !!!')
            target_index = s_recursive(rand_list, 0, len(rand_list)-1, target)

        print(f'List: {rand_list}')
        if target_index is not None:
            print(f'Found {target} in index {target_index+1}')
        else:
            print(f'Cannot find {target} in the list')
    except ValueError:
        print('Invalid input')

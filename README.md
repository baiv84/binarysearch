# Файл search.py

В данном модуле реализован классический алгоритм бинарного поиска целого числа в отсортированном массиве чисел (тип `int`). 

На каждом шаге такого поиска число оставшихся элементов для поиска сокращается в 2 раза.

Данный алгоритм имеет сложность `O(log n)`.

## Функция s

Принимает на вход 2 аргумента: 
* последовательность отсортированных целых чисел; 
* число, которое необходимо найти в последовательности - `(образец)`.

Задаются начальные границы поиска - [0; Длина последовательности - 1].

Затем запускается цикл поиска образца среди элементов последовательности.

На каждом шаге цикла образец сравнивается с элементом последовательности, расположенным посередине (медиана).

Если образец больше медианы, то левая граница поиска смещается в сторону медианы, затем происходит переход на новую итерацию цикла. 

Если образец меньше медианы, то правая граница поиска смещается в сторону медианы, затем происходит переход на новую итерацию цикла.

В случае равенства образца и медианы - поиск завершается, возвращается значение медианы в качестве результата поиска.

Цикл завершается сам собой, когда левая граница поиска превышает правую границу.
В этом случае, элемент последовательности не найден, в качестве результата поиска возвращается значение `None`


## Функция Main

В начале генерируется отсортированная последовательность целых чисел от 0 до 100.

Количество элементов последовательности - 10.

Далее, пользователь вводит число - образец для поиска. Затем происходит вызов функции поиска.  

Если возвращается значение, отличное от `None` - образец найден. Выводится сообщение, в котором выводится номер(индекс) найденного элемента в последовательности.

Если возвращается значение `None` - образец не найден. Выводится отладочное сообщение.

В случае ввода пользователем некорректного значения образца для поиска происходит обработка исключительной ситуации - печатается отладочное сообщение о не корректном вводе данных.

- - -

###  `search.py`

```python
from random import sample


def s(list_, target):
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


if __name__ == "__main__":
    list_len = 10
    rand_list = sorted(sample(range(0, 101, 2), list_len))

    try:
        target = int(input('Pick a number between 0-100: '))
        target_index = s(rand_list, target)

        print(f'List: {rand_list}')
        if target_index is not None:
            print(f'Found {target} in index {target_index}')
        else:
            print(f'Cannot find {target} in the list')
    except ValueError:
        print('Invalid input')
```

- - -

### `search_fixed.py`

```python
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
```

import numpy as np
from numpy import array


def replace_element_by_comparison(given_array: array, number: int, action: str, replacement: int) -> array:
    """
    The function checks switches values in array to a given number if a value meets the condition of the operator.
    :param given_array: A numpy array
    :param number: A given integer number.
    :param action: An operator < , > or ==
    :param replacement: A given number to replace.
    :return:
    """
    return{
        '>': np.where(given_array > number, replacement, given_array),
        '<': np.where(given_array < number, replacement, given_array),
        '==': np.where(given_array == number, replacement, given_array),
    }[action]


if __name__ == "__main__":
    print(replace_element_by_comparison(np.arange(5), 4, '==', 8))
    print(replace_element_by_comparison(np.arange(5), 2, '<', 0))
    print(replace_element_by_comparison(np.arange(5), 3, '>', 9))

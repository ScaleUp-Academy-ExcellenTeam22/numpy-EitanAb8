import numpy as np
from numpy import array


def calculate_median(given_array: array) -> array:
    """
    The function compute the median of flattened given array.
    :param given_array: The given array.
    :return: The median flattened.
    """
    return np.median(given_array)


if __name__ == "__main__":
    print(calculate_median(np.arange(25).reshape((5, 5))))

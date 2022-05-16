import numpy as np
from numpy import array


def convert_two_1d_to_one_2d(first_array: array, second_array: array) -> array:
    """
    The function converts (in sequence depth wise (along third axis)) two 1-D arrays into a 2-D array.
    :param first_array: 1-D array.
    :param second_array: 1-D array.
    :return: 2-D array.
    """
    return np.dstack((first_array, second_array)).shape


if __name__ == "__main__":
    print(convert_two_1d_to_one_2d(np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8])))

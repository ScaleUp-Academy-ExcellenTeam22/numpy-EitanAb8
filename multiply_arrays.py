import numpy as np
from numpy import array


def multiply_arrays(first_array: array, second_array: array) -> array:
    """
    The function multiplies two given array's. The array's must be with equiv size.
    :param first_array: First array.
    :param second_array: Second array.
    :return: A result array of the multiplication of the two given array's
    """
    return np.multiply(first_array, second_array)


if __name__ == "__main__":
    print(multiply_arrays(np.arange(5), np.zeros(5)))

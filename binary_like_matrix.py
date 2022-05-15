import numpy as np
from numpy import array


def binary_like_matrix() -> array:
    """
    The function creates a matrix of 10x10, in which the elements on the borders will be equal to 1, and inside 0
    :return: A 10x10 matrix wrapped with 1's and filled with 0's.
    """
    matrix = np.ones((10, 10), dtype='int')
    matrix[1:-1, 1:-1] = 0
    return matrix


if __name__ == "__main__":
    printbinary_like_matrix())

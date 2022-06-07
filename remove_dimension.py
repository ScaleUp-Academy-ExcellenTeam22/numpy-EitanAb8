import numpy as np
from numpy import array


def remove_dimension(matrix: array) -> array:
    """
    The function removes a single-dimensional entries from a specified shape.
    :param matrix: A given matrix.
    :return: The matrix with less dimensional entry.
    """
    return np.squeeze(matrix)


if __name__ == "__main__":
    print(remove_dimension([[1, 2, 3], [4, 5, 6]]))

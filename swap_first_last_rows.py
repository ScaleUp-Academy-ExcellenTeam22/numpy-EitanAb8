import numpy as np
from numpy import array


def create_4_on_4_matrix() -> array:
    """
    The function creates a 4x4 matrix with values from 0-16.
    :return: A 4x4 matrix;
    """
    return np.arange(16).reshape(4, 4)


def swap_first_last_rows_matrix(matrix: array) -> array:
    """
    The function returns a new matrix like the given matrix swapping the first and last rows.
    :param matrix: A matrix.
    :return: swapped first and last row matrix from the given one.
    """
    swapped_matrix = np.copy(matrix)
    swapped_matrix[0] = matrix[matrix.shape[0]-1]
    swapped_matrix[swapped_matrix.shape[0]-1] = matrix[0]
    return swapped_matrix


if __name__ == "__main__":
    print(swap_first_last_rows_matrix(create_4_on_4_matrix()))

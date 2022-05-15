import numpy as np
from numpy import array


def find_dimensions_of_matrix(matrix: array) -> str:
    """
    The function finds the number of rows and cols of a given matrix
    :param matrix: A given matrix.
    :return: A string indicates the rows and cols of the given matrix.
    """
    return f"The number of rows and cols of the given matrix are: {matrix.shape}"


if __name__ == "__main__":
    print(find_dimensions_of_matrix(np.arange(20).reshape(4, 5)))

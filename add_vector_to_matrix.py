import numpy as np
from numpy import array


def add_vector_to_matrix(matrix: array, vector: array) -> array:
    """
    The function adds a given vector to each row of a given matrix. (vector size must be equiv to row size)
    :param matrix: A given matrix.
    :param vector: A given vector.
    :return: A matrix with the given matrix's values + the vector values added to each row.
    """
    return matrix+vector


if __name__ == "__main__":
    print(add_vector_to_matrix(np.ones(20).reshape(4, 5), np.ones(5)))

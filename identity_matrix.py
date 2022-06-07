import numpy as np
from numpy import array


def identity_matrix(size: int) -> array:
    """
    The function creates an identity matrix with a dimension of a given size.
    :param size: An integer represent the size of the matrix.
    :return: An identity matrix with a dimension of the given size.
    """
    return np.eye(size)


if __name__ == "__main__":
    print(identity_matrix(3))

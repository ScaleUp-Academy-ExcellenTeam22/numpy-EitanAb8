import numpy as np
from numpy import array


def combine_arrays(first_array: array, second_array: array) -> None:
    """
    The function combines a one and a two dimensional array together and display their elements.
    :param first_array: An array.
    :param second_array: An array.
    :return: None.
    """
    for first, second in np.nditer([first_array, second_array]):
        print(f"{first} : {second}")


if __name__ == "__main__":
    combine_arrays(np.array([0, 1, 2, 3]), np.array([[0, 1, 2, 3], [4, 5, 6, 7]]))

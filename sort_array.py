import numpy as np
from numpy import array


def sort_array(given_array: array) -> str:
    """
    The function sorts an array by first axis and last axis.
    :param given_array: A given array.
    :return: A string of the results of sorting the array by first axis and last axis.
    """
    return (f"Original array:\n {given_array} \n"
            f"Sort along the first axis:\n {np.sort(given_array, axis=0)}.\n "
            f"Sort along the last axis:\n {np.sort(np.sort(given_array, axis=0), axis=1)}")


if __name__ == "__main__":
    print(sort_array(np.array([[4, 6], [2, 1]])))

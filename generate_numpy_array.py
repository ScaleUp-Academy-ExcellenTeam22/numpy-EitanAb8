import numpy as np
from numpy import array


def generate_numpy_array() -> array:
    """
    The function generates a numpy array with values from 0-20.
    Then it changes the sign of the numbers in the range from 0 to 15.
    :return: A numpy array
    """
    return np.concatenate((np.arange(9), (np.arange(7)+9)*-1, (np.arange(5)+16)))


if __name__ == "__main__":
    print(generate_numpy_array())

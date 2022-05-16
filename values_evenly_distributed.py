import numpy as np
from numpy import array


def values_evenly_distributed() -> array:
    """
    The function generates a numpy array of range 10,
    and generates values evenly distributed from 5 to 50.
    :return: A numpy array
    """
    return np.linspace(5, 50, 10, dtype='int')


if __name__ == "__main__":
    print(values_evenly_distributed())

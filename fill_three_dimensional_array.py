import numpy as np
from numpy import array


def fill_three_dimensional_array() -> array:
    """
    The function creates a three-dimension array with shape (300,400,5) and set fills
    the array elements with values using unsigned integer (0 to 255).
    :return: An 3D array with values from 0 to 255.
    """
    return np.random.randint(low=0, high=255, size=(300, 400, 5))


if __name__ == "__main__":
    print(fill_three_dimensional_array())

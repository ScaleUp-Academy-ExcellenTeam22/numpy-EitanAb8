import numpy as np
from numpy import array


def sort_students(id_array: array, height_array: array) -> array:
    """
    The function sort the student id with increasing height of the students from given students id and height
    and then prints the integer indices that describes the sort order by multiple columns and the sorted data.
    :param id_array: An array of the students id.
    :param height_array: An array of the students height.
    :return: An array of integer indices describes the sort order.
    """
    return np.lexsort((id_array, height_array))


if __name__ == "__main__":
    print(sort_students(np.array([3122, 3156, 3018]), np.array([180, 150, 170])))

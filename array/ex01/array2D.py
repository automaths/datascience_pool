import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array from start to end (not included)
    :param family: 2D array
    :param start: start index
    :param end: end index
    :return: 2D array
    """
    my_array = np.array(family)
    if my_array.ndim != 2:
        print("family is not a 2D array")
        return []
    if start >= len(my_array) or end > len(my_array):
        print("start and end must be smaller than the length of family")
        return []
    if start == end:
        print("start and end must be different")
        return []
    if start == 0 and end == len(my_array):
        print("no need to slice family")
        return family
    for row in my_array:
        if len(row) is not len(my_array[0]):
            print("all lines of family must have the same length")
            return []


    print(f"My shape is {my_array.shape}")
    my_array = my_array[start:end]
    print(f"My new shape is {my_array.shape}")
    return my_array.tolist()

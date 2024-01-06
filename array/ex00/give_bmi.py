import numpy as np 

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Returns the BMI of each person in the list.

    Args:
        height (list[int | float]): List of heights.
        weight (list[int | float]): List of weights.

    Returns:
        list[int | float]: List of BMI.
    """
    if len(height) != len(weight):
        print("The length of the lists must be the same.")
        return []
    if len(height) == 0:
        print("The lists must not be empty.")
        return []
    if min(height) <= 0 or min(weight) <= 0:
        print("The values must be positive.")
        return []
    for item in height:
        if (type(item) is not int and type(item) is not float):
            print("The height lists must contain only int or float.")
            return []
    for item in weight:
        if (type(item) is not int and type(item) is not float):
            print("The weight lists must contain only int or float.")
            return []
    return np.array(weight) / np.array(height) ** 2


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Returns a list of booleans indicating whether the BMI is above the limit.

    Args:
        bmi (list[int | float]): List of BMI.
        limit (int): Limit to apply.

    Returns:
        list[bool]: List of booleans.
    """
    return np.array(bmi) > limit
import numpy as np      # https://numpy.org


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values from height and weight lists.

    Args:
        height: List of heights in meters.
        weight: List of weights in kilograms.

    Returns:
        List of BMI values calculated as weight / (height^2).

    Raises:
        TypeError: If inputs are not lists or contain invalid types.
        ValueError: If lists have different lengths or height contains 0.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be lists.")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")

    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("All height values must be int or float.")

    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("All weight values must be int or float.")

    if any(h == 0 for h in height):
        raise ValueError("Height values must not be zero.")

    # Convert input lists to NumPy arrays for efficient element-wise operations
    height_array = np.array(height)
    weight_array = np.array(weight)
    bmi_array = weight_array / (height_array ** 2)

    return bmi_array.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if BMI values are above a given limit.

    Args:
        bmi: A list of BMI values.
        limit: Integer limit to compare against.

    Returns:
        List of booleans indicating if each BMI is above the limit.

    Raises:
        TypeError: If bmi is not a list, contains invalid types
        or limit is not an integer.
    """
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list.")

    if not all(isinstance(x, (int, float)) for x in bmi):
        raise TypeError("All BMI values must be int or float.")

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")

    # Convert input lists to NumPy arrays for efficient element-wise operations
    bmi_array = np.array(bmi)

    # Perform element-wise comparison and convert result back to a regular list
    return (bmi_array > limit).tolist()

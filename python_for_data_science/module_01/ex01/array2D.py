import numpy as np      # https://numpy.org


def slice_me(family: list, start: int, end: int) -> list:
    """"
    Takes a 2D array and returns a truncated version based on the provided
    start and end arguments using slicing.

    Args:
        family: A 2D list.
        start: Start index for slicing.
        end: End index for slicing.

    Returns:
        list: A sliced 2D list.

    Raises:
        TypeError: If input validation fails.
    """
    if not isinstance(family, list):
        raise TypeError("Family must be a list.")

    if not all(isinstance(row, list) for row in family):
        raise TypeError("Each row must be a list.")

    if not all(len(row) == len(family[0]) for row in family):
        raise TypeError("All rows must be of the same length.")

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Both start and end must be integers.")

    # Convert to NumPy array
    family_array = np.array(family)
    print(f"My shape is : {family_array.shape}")

    # Perform slicing
    sliced_array = family_array[start:end]
    print(f"My new shape is : {sliced_array.shape}")

    return sliced_array.tolist()

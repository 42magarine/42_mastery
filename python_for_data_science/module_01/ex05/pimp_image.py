import numpy as np                  # https://numpy.org
import matplotlib.pyplot as plt     # https://matplotlib.org


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of an image by subtracting each pixel value from 255.

    Args:
        array: 3D NumPy array representing an RGB image.

    Returns:
        np.ndarray: Image with inverted colors.
    """
    inverted = array.copy()
    inverted[:, :, 0] = 255 - inverted[:, :, 0]
    inverted[:, :, 1] = 255 - inverted[:, :, 1]
    inverted[:, :, 2] = 255 - inverted[:, :, 2]
    # inverted = 255 - inverted

    plt.imshow(inverted)
    plt.savefig("./img/inverted.jpeg")
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applies a red filter to an image by setting green and blue channels to 0.

    Args:
        array: 3D NumPy array representing an RGB image.

    Returns:
        np.ndarray: Image with only the red channel preserved.
    """
    red_filtered = array.copy()
    red_filtered[:, :, 1] = red_filtered[:, :, 1] * 0
    red_filtered[:, :, 2] = red_filtered[:, :, 2] * 0
    # red_filtered = red_filtered * [1, 0, 0]

    plt.imshow(red_filtered)
    plt.savefig("./img/red_filtered.jpeg")
    return red_filtered


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to an image by setting red and blue channels to 0.

    Args:
        array: 3D NumPy array representing an RGB image.

    Returns:
        np.ndarray: Image with only the green channel preserved.
    """
    green_filtered = array.copy()
    green_filtered[:, :, 0] = green_filtered[:, :, 0] - green_filtered[:, :, 0]
    green_filtered[:, :, 2] = green_filtered[:, :, 2] - green_filtered[:, :, 2]

    plt.imshow(green_filtered)
    plt.savefig("./img/green_filtered.jpeg")
    return green_filtered


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applies a blue filter to an image by setting red and green channels to 0.

    Args:
        array: 3D NumPy array representing an RGB image.

    Returns:
        np.ndarray: Image with only the blue channel preserved.
    """
    blue_filtered = array.copy()
    blue_filtered[:, :, 0] = 0
    blue_filtered[:, :, 1] = 0

    plt.imshow(blue_filtered)
    plt.savefig("./img/blue_filtered.jpeg")
    return blue_filtered


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts an image to grayscale by averaging RGB values across all channels.

    Args:
        array: 3D NumPy array representing an RGB image.

    Returns:
        np.ndarray: Grayscale image.
    """
    # Better approach: direct division without intermediate variable
    gray_value = (array[:, :, 0] + array[:, :, 1] + array[:, :, 2]) / 3

    grey_filtered = array.copy()
    grey_filtered[:, :, 0] = gray_value
    grey_filtered[:, :, 1] = gray_value
    grey_filtered[:, :, 2] = gray_value

    plt.imshow(grey_filtered)
    plt.savefig("./img/grey_filtered.jpeg")
    return grey_filtered

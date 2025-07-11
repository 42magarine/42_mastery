#!/usr/bin/env python

import numpy as np                  # https://numpy.org
import matplotlib.pyplot as plt     # https://matplotlib.org
from load_image import ft_load


def transpose(image_array: np.ndarray) -> np.ndarray:
    """
    Manually transpose a 2D image array.

    Args:
        image_array (np.ndarray): Input 2D image array (shape: height x width).

    Returns:
        np.ndarray: Transposed array (shape: width x height)
    """
    height, width = image_array.shape

    # Create an empty array with swapped dimensions (width, height)
    transposed = np.zeros((width, height), dtype=image_array.dtype)

    # Swap rows and columns
    for y in range(height):
        for x in range(width):
            transposed[x][y] = image_array[y][x]

    return transposed


def main():
    """
    Load an image, extract a centered 400x400 zoom,
    convert one color channel to grayscale, transpose and save it.

    Raises:
        Exception: Any error during image loading, processing, or saving.
    """
    try:
        # Load the original image as a NumPy array
        image_array = ft_load("animal.jpeg")
        print(image_array)

        # Define zoom dimensions
        zoom_height = 400
        zoom_width = 400

        # Get original image dimensions
        height, width = image_array.shape[:2]

        # Calculate centered crop coordinates
        start_y = max(0, (height - zoom_height) // 2)
        start_x = max(0, (width - zoom_width) // 2)
        end_y = min(start_y + zoom_height, height)
        end_x = min(start_x + zoom_width, width)

        # Extract the zoomed region from the original image
        zoomed_image = image_array[start_y:end_y, start_x:end_x]

        # Convert to grayscale by selecting one color channel
        gray_image = zoomed_image[:, :, 0]    # Red
        # gray_image = zoomed_image[:, :, 1]    # Green
        # gray_image = zoomed_image[:, :, 2]    # Blue

        # Manual transpose image
        transposed_image = transpose(gray_image)

        # Display shape and pixel data
        print(f"New shape after Transpose: {transposed_image.shape}")
        print(transposed_image)

        # Plot the grayscale image ('cmap' renders grayscale)
        plt.imshow(transposed_image, cmap='gray')

        # Save image
        plt.savefig("transposed.jpeg")

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()


# Original:     Transpose:      90° Rotation(left):     90° Rotation(right):
# [1 2 3]       [1 4 7]         [3 6 9]                 [7 4 1]
# [4 5 6]       [2 5 8]    vs   [2 5 8]     vs          [8 5 2]
# [7 8 9]       [3 6 9]         [1 4 7]                 [9 6 3]

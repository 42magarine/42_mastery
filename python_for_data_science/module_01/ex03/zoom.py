#!/usr/local/bin/python3

import matplotlib.pyplot as plt     # https://matplotlib.org
from load_image import ft_load


def main():
    """
    Load an image, extract a centered 400x400 zoom,
    convert one color channel to grayscale and save it.

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

        # Display shape and pixel data
        print(f"New shape after slicing: {gray_image.shape}")
        print(gray_image)

        # Plot the grayscale image ('cmap' renders grayscale)
        plt.imshow(gray_image, cmap='gray')

        # Save image
        plt.savefig("zoomed.jpeg")

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()

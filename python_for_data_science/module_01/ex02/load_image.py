import os
import numpy as np      # https://numpy.org
from PIL import Image   # https://pillow.readthedocs.io/en/stable


def ft_load(path: str) -> np.ndarray:
    """
    Load an image and return its RGB pixel data as a numpy array.

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray: 3D NumPy array with RGB pixel values.

    Raises:
        TypeError: If path is not a string.
        FileNotFoundError: If the file doesn't exist.
        ValueError: If the file format is not supported.
    """
    if not isinstance(path, str):
        raise TypeError("Path must be a string.")

    if not os.path.isfile(path):
        raise FileNotFoundError(f"File '{path}' not found.")

    with Image.open(path) as img:
        if img.format not in ["JPG", "JPEG"]:
            raise ValueError("Only .jpg or .jpeg images are supported.")

        # Convert to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Convert to numpy array
        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")
        # img_array[y][x][channel]
        #           ↑  ↑  ↑
        #        Zeile |  |
        #           Spalte|
        #              Farbe (0=Rot, 1=Grün, 2=Blau)

        return img_array

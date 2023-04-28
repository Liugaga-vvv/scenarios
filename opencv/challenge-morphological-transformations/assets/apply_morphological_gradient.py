import cv2
import numpy as np


def apply_morphological_gradient(
    image: np.ndarray, kernel_shape: str, kernel_size: int
) -> np.ndarray:
    """
    Applies a morphological gradient operation to the input binary image.

    Args:
    image (np.ndarray): The binary image.
    kernel_shape (str): The shape of the structuring element (rectangular, elliptical, or cross).
    kernel_size (int): The size of the structuring element.

    Returns:
    np.ndarray: The processed image.
    """
    # TODO: implement this function here.
    # Note: Do not change the existing code.

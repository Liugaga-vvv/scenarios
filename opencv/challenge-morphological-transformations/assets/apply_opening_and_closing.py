import cv2
import numpy as np


def apply_opening_and_closing(
    image: np.ndarray,
    kernel_shape: str,
    kernel_size: int,
    opening_iterations: int,
    closing_iterations: int,
) -> np.ndarray:
    """
    Applies opening and closing operations to the input binary image.

    Args:
    image (np.ndarray): The binary image.
    kernel_shape (str): The shape of the structuring element (rectangular, elliptical, or cross).
    kernel_size (int): The size of the structuring element.
    opening_iterations (int): The number of opening iterations to apply.
    closing_iterations (int): The number of closing iterations to apply.

    Returns:
    np.ndarray: The processed image.
    """
    # TODO: implement this function here.
    # Note: Do not change the existing code.

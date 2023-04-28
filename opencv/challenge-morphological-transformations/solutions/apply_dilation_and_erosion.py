import cv2
import numpy as np
import random


def apply_dilation_and_erosion(
    image: np.ndarray,
    kernel_shape: str,
    kernel_size: int,
    dilation_iterations: int,
    erosion_iterations: int,
) -> np.ndarray:
    """
    Applies dilation and erosion operations to the input binary image.

    Args:
    image (np.ndarray): The binary image.
    kernel_shape (str): The shape of the structuring element (rectangular, elliptical, or cross).
    kernel_size (int): The size of the structuring element.
    dilation_iterations (int): The number of dilation iterations to apply.
    erosion_iterations (int): The number of erosion iterations to apply.

    Returns:
    np.ndarray: The processed image.
    """
    if kernel_shape == "rectangular":
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    elif kernel_shape == "elliptical":
        kernel = cv2.getStructuringElement(
            cv2.MORPH_ELLIPSE, (kernel_size, kernel_size)
        )
    elif kernel_shape == "cross":
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))

    dilated_image = cv2.dilate(image, kernel, iterations=dilation_iterations)
    eroded_image = cv2.erode(dilated_image, kernel, iterations=erosion_iterations)

    return eroded_image

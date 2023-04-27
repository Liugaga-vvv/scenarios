import cv2
from typing import Tuple


def load_and_convert_images(
    source_path: str, template_path: str
) -> Tuple[cv2.Mat, cv2.Mat]:
    """
    Load the source image and template image, then convert them to grayscale.

    Args:
        source_path (str): Path to the source image.
        template_path (str): Path to the template image.

    Returns:
        Tuple[cv2.Mat, cv2.Mat]: A tuple containing the grayscale source image and grayscale template image.
    """
    source_image = cv2.imread(source_path)
    template_image = cv2.imread(template_path)

    gray_source = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    return gray_source, gray_template

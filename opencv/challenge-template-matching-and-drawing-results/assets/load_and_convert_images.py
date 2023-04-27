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
    # TODO: implement this function here.
    # Note: Do not change the existing code.

    return gray_source, gray_template


# # You can use the following code to save the grayscale results as the files "gray_source.jpg" and "gray_template.jpg".
# path1 = "test_source.jpg"
# path2 = "test_template.jpg"
# img1, img2 = load_and_convert_images(path1, path2)
# # save files
# cv2.imwrite("gray_source.jpg", img1)
# cv2.imwrite("gray_template.jpg", img2)
# # The grayscale result files you generate can be used in the next challenge perform_template_matchingz.

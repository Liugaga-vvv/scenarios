import cv2
from typing import Dict, Tuple


def perform_template_matching(
    gray_source: cv2.Mat, gray_template: cv2.Mat
) -> Dict[str, Tuple[float, Tuple[int, int]]]:
    """
    Perform template matching using multiple methods and find the best match locations.

    Args:
        gray_source (cv2.Mat): Grayscale source image.
        gray_template (cv2.Mat): Grayscale template image.

    Returns:
        Dict[str, Tuple[float, Tuple[int, int]]]: A dictionary containing the best match score and location for each method.
    """

    methods = {
        "cv2.TM_SQDIFF_NORMED": cv2.TM_SQDIFF_NORMED,
        "cv2.TM_CCOEFF_NORMED": cv2.TM_CCOEFF_NORMED,
        "cv2.TM_CCORR_NORMED": cv2.TM_CCORR_NORMED,
    }

    best_matches = {}

    # TODO: implement this function here.
    # Note: Do not change the existing code.

    return best_matches


# # You can use the following code to test your function.
# # You can generate the files "gray_source.jpg" and "gray_template.jpg" in the previous challenge.
# path1 = "gray_source.jpg"
# path2 = "gray_template.jpg"
# img1 = cv2.imread(path1, cv2.COLOR_BGR2GRAY)
# img2 = cv2.imread(path2, cv2.COLOR_BGR2GRAY)
# best_matches = perform_template_matching(img1,img2)
# # Print the results of your template match.
# print(best_matches)

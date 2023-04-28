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

    for method in methods.keys():
        result = cv2.matchTemplate(gray_source, gray_template, methods[method])
        minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(result)
        if method == "cv2.TM_SQDIFF_NORMED":
            best_matches[method] = (minValue, minLoc)
        else:
            best_matches[method] = (maxValue, maxLoc)
    return best_matches

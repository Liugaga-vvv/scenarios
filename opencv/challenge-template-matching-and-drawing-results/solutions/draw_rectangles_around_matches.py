import cv2
import numpy as np
from typing import Dict, Tuple


def draw_rectangles_around_matches(
    source_image: cv2.Mat,
    template_image: cv2.Mat,
    best_matches: Dict[str, Tuple[float, Tuple[int, int]]],
) -> Tuple[np.ndarray]:
    """
    Draw rectangles around the best matches for each template matching method.

    Args:
        source_image (cv2.Mat): Original source image.
        template_image (cv2.Mat): Original template image.
        best_matches (Dict[str, Tuple[float, Tuple[int, int]]]): Dictionary containing the best match score and location for each method.

    Returns:
        Dict[str, cv2.Mat]: Dictionary containing the image after drawing rectangle.
    """
    template_width, template_height = template_image.shape[:2]
    colors = {
        "cv2.TM_SQDIFF_NORMED": (0, 255, 0),
        "cv2.TM_CCOEFF_NORMED": (255, 0, 0),
        "cv2.TM_CCORR_NORMED": (0, 0, 255),
    }
    matches_list = [m for m in best_matches.items()]
    method1, (Value1, Loc1) = matches_list[0]
    method2, (Value2, Loc2) = matches_list[1]
    method3, (Value3, Loc3) = matches_list[2]
    top_left1 = Loc1
    bottom_right1 = (top_left1[0] + template_height, top_left1[1] + template_width)
    top_left2 = Loc2
    bottom_right2 = (top_left2[0] + template_height, top_left2[1] + template_width)
    top_left3 = Loc3
    bottom_right3 = (top_left3[0] + template_height, top_left3[1] + template_width)
    source_with_rectangles1 = cv2.rectangle(
        source_image.copy(), top_left1, bottom_right1, colors[method1], 2
    )
    source_with_rectangles2 = cv2.rectangle(
        source_image.copy(), top_left2, bottom_right2, colors[method2], 2
    )
    source_with_rectangles3 = cv2.rectangle(
        source_image.copy(), top_left3, bottom_right3, colors[method3], 2
    )
    result = {
        "cv2.TM_SQDIFF_NORMED": source_with_rectangles1,
        "cv2.TM_CCOEFF_NORMED": source_with_rectangles2,
        "cv2.TM_CCORR_NORMED": source_with_rectangles3,
    }
    return result

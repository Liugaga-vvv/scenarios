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

    # TODO: implement this function here.
    # Note: Do not change the existing code.

    result = {
        "cv2.TM_SQDIFF_NORMED": source_with_rectangles1,
        "cv2.TM_CCOEFF_NORMED": source_with_rectangles2,
        "cv2.TM_CCORR_NORMED": source_with_rectangles3,
    }
    return result


# # You can use the following code to test your function.
# from perform_template_matching import perform_template_matching
# path1 = "test_source.jpg"
# path2 = "test_template.jpg"
# img1 = cv2.imread(path1)
# img2 = cv2.imread(path2)
# best_matches = perform_template_matching(img1,img2)
# img_1, img_2, img_3 = draw_rectangles_around_matches(img1, img2, best_matches).values()
# # Save the drawing results using the three methods as "img_1.jpg", "img_2.jpg", "img_3.jpg"
# cv2.imwrite("img_1.jpg", img_1)
# cv2.imwrite("img_2.jpg", img_2)
# cv2.imwrite("img_3.jpg", img_3)

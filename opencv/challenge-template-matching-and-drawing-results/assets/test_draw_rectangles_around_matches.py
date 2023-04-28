import unittest
import cv2
import inspect
import os

import sys

sys.path.append("/home/labex/project")
from draw_rectangles_around_matches import draw_rectangles_around_matches


class TestTemplateMatching(unittest.TestCase):
    def test_draw_rectangles_around_matches(self):
        source_image = cv2.imread("test_source2.jpg")
        template_image = cv2.imread("test_template2.jpg")

        best_matches = {
            "cv2.TM_SQDIFF_NORMED": (1.0, (10, 20)),
            "cv2.TM_CCOEFF_NORMED": (0.8, (30, 40)),
            "cv2.TM_CCORR_NORMED": (0.6, (50, 60)),
        }
        colors = {
            "cv2.TM_SQDIFF_NORMED": (0, 255, 0),
            "cv2.TM_CCOEFF_NORMED": (255, 0, 0),
            "cv2.TM_CCORR_NORMED": (0, 0, 255),
        }

        result = draw_rectangles_around_matches(
            source_image, template_image, best_matches
        )
        source_lines, _ = inspect.getsourcelines(draw_rectangles_around_matches)
        target = False
        for line in source_lines:
            if "cv2.rectangle" in line:
                target = True
            else:
                pass
        self.assertTrue(target)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 3)

        for m in best_matches.keys():
            self.assertIn(m, result)
            self.assertEqual(result[m].shape, source_image.shape)
            self.assertTrue((result[m] != source_image).sum() != 0)


if __name__ == "__main__":
    unittest.main()

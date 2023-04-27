import unittest
import cv2
import inspect
import sys

sys.path.append("/home/labex/project")
from perform_template_matching import perform_template_matching


class TestTemplateMatching(unittest.TestCase):
    def test_perform_template_matching(self):
        gray_source = cv2.imread("/tmp/gray_test_source2.jpg", cv2.COLOR_BGR2GRAY)
        gray_template = cv2.imread("/tmp/gray_test_template2.jpg", cv2.COLOR_BGR2GRAY)
        methods = {
            "cv2.TM_SQDIFF_NORMED": cv2.TM_SQDIFF_NORMED,
            "cv2.TM_CCOEFF_NORMED": cv2.TM_CCOEFF_NORMED,
            "cv2.TM_CCORR_NORMED": cv2.TM_CCORR_NORMED,
        }

        best_matches = perform_template_matching(gray_source, gray_template)

        source_lines, _ = inspect.getsourcelines(perform_template_matching)
        target = False
        for line in source_lines:
            if "cv2.matchTemplate" in line:
                target = True
            else:
                pass

        self.assertTrue(target)
        self.assertIsInstance(best_matches, dict)
        self.assertEqual(len(best_matches), 3)
        for m in methods.keys():
            self.assertIn(m, best_matches)
            self.assertEqual(len(best_matches[m]), 2)
            self.assertEqual(len(best_matches[m][1]), 2)


if __name__ == "__main__":
    unittest.main()

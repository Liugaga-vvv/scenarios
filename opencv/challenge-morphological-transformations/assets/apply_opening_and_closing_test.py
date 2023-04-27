import unittest
import cv2
import numpy as np
import inspect
import sys

sys.path.append("/home/labex/project")
from apply_opening_and_closing import apply_opening_and_closing


class TestMorphologicalTransformations(unittest.TestCase):
    def test_apply_opening_and_closing(self):
        source_lines, _ = inspect.getsourcelines(apply_opening_and_closing)
        target = False
        for line in source_lines:
            if "cv2.getStructuringElement" in line:
                target = True
            elif "cv2.morphologyEx" in line:
                target = True
            else:
                pass
        self.assertTrue(target)
        image = cv2.imread("/tmp/img_test.jpg", cv2.IMREAD_GRAYSCALE)
        kernel_shape, kernel_size, opening_iterations, closing_iterations = (
            "rectangular",
            3,
            2,
            2,
        )
        processed_image = apply_opening_and_closing(
            image, kernel_shape, kernel_size, opening_iterations, closing_iterations
        )
        self.assertIsInstance(processed_image, np.ndarray)
        self.assertEqual(processed_image.shape, image.shape)
        self.assertTrue(np.any(processed_image))
        self.assertTrue((image != processed_image).sum() != 0)


if __name__ == "__main__":
    unittest.main()

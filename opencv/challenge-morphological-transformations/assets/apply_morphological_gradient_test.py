import unittest
import cv2
import numpy as np
import inspect
import sys

sys.path.append("/home/labex/project")
from apply_morphological_gradient import apply_morphological_gradient


class TestMorphologicalTransformations(unittest.TestCase):
    def test_apply_morphological_gradient(self):
        source_lines, _ = inspect.getsourcelines(apply_morphological_gradient)
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
        kernel_shape, kernel_size = "elliptical", 7
        processed_image = apply_morphological_gradient(image, kernel_shape, kernel_size)

        self.assertIsInstance(processed_image, np.ndarray)
        self.assertEqual(processed_image.shape, image.shape)
        self.assertTrue(np.any(processed_image))
        self.assertTrue((image != processed_image).sum() != 0)


if __name__ == "__main__":
    unittest.main()

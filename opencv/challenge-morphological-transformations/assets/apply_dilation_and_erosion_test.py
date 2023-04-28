import unittest
import cv2
import numpy as np

import inspect
import sys

sys.path.append("/home/labex/project")

from apply_dilation_and_erosion import apply_dilation_and_erosion


class TestMorphologicalTransformations(unittest.TestCase):
    def test_apply_dilation_and_erosion(self):
        image = cv2.imread("/tmp/img_test.jpg", cv2.IMREAD_GRAYSCALE)
        for kernel_shape in ["rectangular", "elliptical", "cross"]:
            kernel_size, dilation_iterations, erosion_iterations = 5, 2, 2
            processed_image = apply_dilation_and_erosion(
                image,
                kernel_shape,
                kernel_size,
                dilation_iterations,
                erosion_iterations,
            )
            source_lines, _ = inspect.getsourcelines(apply_dilation_and_erosion)
            target = False
            for line in source_lines:
                if "cv2.getStructuringElement" in line:
                    target = True
                elif "cv2.dilate" in line:
                    target = True
                elif "cv2.erode" in line:
                    target = True
                else:
                    pass
            self.assertTrue(target)
            self.assertIsInstance(processed_image, np.ndarray)
            self.assertEqual(processed_image.shape, image.shape)
            self.assertTrue(np.any(processed_image))
            self.assertTrue((image != processed_image).sum() != 0)


if __name__ == "__main__":
    unittest.main()

import unittest
import cv2
import numpy as np
import inspect
import sys

sys.path.append("/home/labex/project")

from generate_binary_image import generate_binary_image


class TestMorphologicalTransformations(unittest.TestCase):
    def test_generate_binary_image(self):
        width, height, num_shapes = 200, 200, 10
        binary_image = generate_binary_image(width, height, num_shapes)
        source_lines, _ = inspect.getsourcelines(generate_binary_image)
        target = False
        for line in source_lines:
            if " cv2.circle" in line:
                target = True
            elif "cv2.rectangle" in line:
                target = True
            elif "cv2.line" in line:
                target = True
            else:
                pass
        self.assertTrue(target)
        self.assertIsInstance(binary_image, np.ndarray)
        self.assertEqual(set(binary_image.reshape(-1).tolist()), set([0, 255]))


if __name__ == "__main__":
    unittest.main()

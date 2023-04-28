import unittest
import cv2
from typing import Tuple, Dict
import sys

sys.path.append("/home/labex/project")

from load_and_convert_images import load_and_convert_images


class TestTemplateMatching(unittest.TestCase):
    def test_load_and_convert_images(self):
        source_path = "/tmp/test_source2.jpg"
        template_path = "/tmp/test_template2.jpg"

        gray_source1, gray_template1 = load_and_convert_images(
            source_path, template_path
        )

        source_image = cv2.imread(source_path)
        template_image = cv2.imread(template_path)
        gray_source2 = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
        gray_template2 = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
        self.assertEqual((gray_source1 != gray_source2).sum(), 0)
        self.assertEqual((gray_template1 != gray_template2).sum(), 0)


if __name__ == "__main__":
    unittest.main()

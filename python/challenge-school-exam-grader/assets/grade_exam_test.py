import sys

sys.path.append("/home/labex/project")

import unittest
import time
from grade_exam import grade_exam


class TestGradeExam(unittest.TestCase):
    def test_grade_exam(self):
        exam_scores1 = [85, 92, 78, 65, 90, 100, 70, 75, 82, 95]
        grade_dict1 = grade_exam(exam_scores1)
        self.assertEqual(grade_dict1["date"], time.strftime("%m/%d/%Y"))
        self.assertEqual(grade_dict1["A"], 4)
        self.assertEqual(grade_dict1["B"], 2)
        self.assertEqual(grade_dict1["C"], 3)
        self.assertEqual(grade_dict1["D"], 1)
        self.assertEqual(grade_dict1["F"], 0)

        exam_scores2 = [60, 70, 80, 90, 100]
        grade_dict2 = grade_exam(exam_scores2)
        self.assertEqual(grade_dict2["date"], time.strftime("%m/%d/%Y"))
        self.assertEqual(grade_dict2["A"], 2)
        self.assertEqual(grade_dict2["B"], 1)
        self.assertEqual(grade_dict2["C"], 1)
        self.assertEqual(grade_dict2["D"], 1)
        self.assertEqual(grade_dict2["F"], 0)


if __name__ == "__main__":
    unittest.main()

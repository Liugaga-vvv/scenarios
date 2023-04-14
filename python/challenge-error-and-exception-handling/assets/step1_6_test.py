import sys

sys.path.append("/home/labex/project")

import unittest, os

from custom_exceptions_and_logging import main


class TestStep1(unittest.TestCase):
    def test_process_data_not_file(self):
        os.rename(
            "/home/labex/project/example.txt", "/home/labex/project/example.txt.bac"
        )
        try:
            main()
        except Exception as e:
            raise e
        finally:
            os.rename(
                "/home/labex/project/example.txt.bac", "/home/labex/project/example.txt"
            )

        with open("/home/labex/project/error_handling_challenge.log") as f:
            ctx = f.readlines()

        if len(ctx) != 0:
            self.assertTrue(
                "File /home/labex/project/example.txt not found" in ctx[-1].strip()
            )
        else:
            raise AssertionError("")


if __name__ == "__main__":
    unittest.main()

import unittest
import sys

sys.path.append("/home/labex/project")
from swap_dict import swap_dict_key_value

class TestSwapDictKeyValue(unittest.TestCase):
    
    def test_swap_dict_key_value(self):
        input_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
        expected_output = {v:k for k,v in input_dict.items()}
        self.assertDictEqual(swap_dict_key_value(input_dict), expected_output)
    
    def test_swap_dict_key_value_empty_dict(self):
        input_dict = {}
        self.assertDictEqual(swap_dict_key_value(input_dict), {})
    
    def test_swap_dict_key_value_duplicate_values(self):
        input_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value1'}
        expected_output = {'value1': 'key3', 'value2': 'key2'}
        self.assertDictEqual(swap_dict_key_value(input_dict), expected_output)
    
    def test_swap_dict_key_value_sort_values(self):
        input_dict = {'key1': 'value3', 'key2': 'value2', 'key3': 'value1'}
        expected_output = {'value1': 'key3', 'value2': 'key2', 'value3': 'key1'}
        self.assertDictEqual(swap_dict_key_value(input_dict), expected_output)

if __name__ == '__main__':
    unittest.main()
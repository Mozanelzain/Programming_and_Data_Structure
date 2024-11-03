#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from print import say_my_name

class TestNamePrinter(unittest.TestCase):
    def test_name_formatting(self):
        test_cases = [
            (("Alice", "Smith"), "My name is Alice Smith\n"),
            (("Bob", "Jones"), "My name is Bob Jones\n"),
            (("Carol", ""), "My name is Carol \n"),
            (("David",), "My name is David \n"),
        ]
        
        for inputs, expected in test_cases:
            with self.subTest(inputs=inputs):
                with patch('sys.stdout', new=StringIO()) as fake_out:
                    say_my_name(*inputs)
                    self.assertEqual(fake_out.getvalue(), expected)

    def test_input_validation(self):
        invalid_cases = [
            ((123, "Smith"), TypeError),
            (("John", 456), TypeError),
            ((None,), TypeError),
            (([], "Smith"), TypeError),
            (("John", None), TypeError),
        ]
        
        for inputs, expected_error in invalid_cases:
            with self.subTest(inputs=inputs):
                with self.assertRaises(expected_error):
                    say_my_name(*inputs)

if __name__ == '__main__':
    unittest.main()

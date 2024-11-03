#!/usr/bin/python3
import unittest
from add import add_integer

class TestAddFunction(unittest.TestCase):
    def test_basic_addition(self):
        test_cases = [
            ((5, 5), 10),
            ((1, -1), 0),
            ((-10, -5), -15),
            ((0, 0), 0),
        ]
        for inputs, expected in test_cases:
            with self.subTest(inputs=inputs):
                self.assertEqual(add_integer(*inputs), expected)

    def test_float_conversion(self):
        test_cases = [
            ((3.14, 2.86), 6),
            ((2.5, -2.5), 0),
            ((-1.9, -0.1), -2),
        ]
        for inputs, expected in test_cases:
            with self.subTest(inputs=inputs):
                self.assertEqual(add_integer(*inputs), expected)

    def test_default_parameter(self):
        self.assertEqual(add_integer(2), 100)
        self.assertEqual(add_integer(-98), 0)

    def test_type_validation(self):
        invalid_inputs = [
            ("string", 1),
            (1, "string"),
            (None, 1),
            ([1], 2),
            ((1,), 2),
        ]
        for inputs in invalid_inputs:
            with self.subTest(inputs=inputs):
                with self.assertRaises(TypeError):
                    add_integer(*inputs)

if __name__ == '__main__':
    unittest.main()

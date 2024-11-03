#!/usr/bin/python3
import unittest
from divide import matrix_divided

class TestMatrixDivision(unittest.TestCase):
    def setUp(self):
        self.sample_matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    def test_successful_division(self):
        test_cases = [
            (self.sample_matrix, 2, [
                [0.5, 1.0, 1.5],
                [2.0, 2.5, 3.0],
                [3.5, 4.0, 4.5]
            ]),
            ([[10, 20], [30, 40]], 5, [[2.0, 4.0], [6.0, 8.0]]),
        ]
        for matrix, div, expected in test_cases:
            with self.subTest(matrix=matrix, div=div):
                self.assertEqual(matrix_divided(matrix, div), expected)

    def test_floating_point_division(self):
        matrix = [[1.5, 2.5], [3.5, 4.5]]
        expected = [[0.75, 1.25], [1.75, 2.25]]
        self.assertEqual(matrix_divided(matrix, 2), expected)

    def test_invalid_matrices(self):
        invalid_cases = [
            ("not a matrix", 2),
            ([[1, 2], [3, "4"]], 2),
            ([[1, 2], [3, 4, 5]], 2),
            ([], 2),
            ([[]], 2)
        ]
        for matrix, div in invalid_cases:
            with self.subTest(matrix=matrix, div=div):
                with self.assertRaises((TypeError, ValueError)):
                    matrix_divided(matrix, div)

    def test_invalid_divisors(self):
        invalid_divisors = [0, "2", [2], None]
        for div in invalid_divisors:
            with self.subTest(div=div):
                with self.assertRaises((TypeError, ZeroDivisionError)):
                    matrix_divided(self.sample_matrix, div)

if __name__ == '__main__':
    unittest.main()

import unittest
from typing import Union


def sum_numbers(x1: Union[int, float], x2: Union[int, float]):
    if not (type(x1) is int or type(x1) is float) and type(x1) != type(x2):
        raise TypeError("x1 and x2 must be int or float")

    return x1 + x2


class TestSum(unittest.TestCase):
    def test_sum_int(self):
        """Should return a sum of two integers"""
        result = sum_numbers(3, 4)
        self.assertEqual(result, 7)

    def test_sum_float(self):
        """Should return a sum of two floats"""
        result = sum_numbers(4.5, 6.7)
        self.assertEqual(result, 11.2)

    def test_sum_string(self):
        """Should raise TypeError with a string"""
        with self.assertRaises(TypeError) as assert_raises:
            sum_numbers('a', 7)

        self.assertIsInstance(assert_raises.exception, TypeError)

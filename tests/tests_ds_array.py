import unittest
import inspect
from src.ds_array import Array 

class TestArrayConstructor(unittest.TestCase):

    def test_valid_size(self):
        """Test creating an array with a valid size."""
        sizes = [1, 5, 10, 100]
        types = [int, float, str]

        for size in sizes:
            for typeof in types:
                arr = Array(size, typeof)
                self.assertEqual(arr._max_size, size)
                self.assertEqual(arr._current_size, 0)
                self.assertEqual(len(arr._allocated_cell), size)
                self.assertEqual(arr._iter_position, 0)
                self.assertIsInstance(arr._allocated_cell, list)

    def test_zero_size(self):
        """Test creating an array with size zero (should raise ValueError)."""
        with self.assertRaises(ValueError) as context:
            Array(0, int)
        self.assertEqual(str(context.exception), "Size: 0, must be larger than zero")

    def test_negative_size(self):
        """Test creating an array with a negative size (should raise ValueError)."""
        with self.assertRaises(ValueError) as context:
            Array(-5, float)
        self.assertEqual(str(context.exception), "Size: -5, must be larger than zero")

    def test_non_integer_size(self):
        """Test creating an array with a non-integer size (should raise ValueError)."""
        invalid_sizes = ["abc", 3.14, True]

        for size in invalid_sizes:
            with self.assertRaises(ValueError) as context:
                Array(size, str)
            self.assertTrue(
                str(context.exception).startswith(f"Value: {size}, of type:")
            )
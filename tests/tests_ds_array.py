import unittest
import inspect
from src.ds_array import Array 

class TestArrayConstructor(unittest.TestCase):
    def test_valid_creation(self):
        """Test creating arrays with valid sizes and types."""
        sizes = [0, 1, 5, 10]
        types = [int, float]  # Allowed types for your Array class
        for size in sizes:
            for typeof in types:
                arr = Array(size, typeof)
                self.assertEqual(arr._max_size, size)
                self.assertEqual(arr._current_size, 0)
                self.assertEqual(len(arr._allocated_cell), size)
                self.assertEqual(arr._iter_position, 0)
                self.assertEqual(arr._typeof, typeof)

    def test_invalid_size(self):
        """Test creating arrays with invalid sizes."""
        with self.assertRaises(ValueError):
            Array(-3, float)

    def test_invalid_type(self):
        """Test creating arrays with invalid types."""
        with self.assertRaises(ValueError):
            Array(5, str)  # String type is not allowed in your Array class

    # def test_iteration(self):
        """Test iterating over the array."""
        # arr = Array(5, int)
        # for i, val in enumerate(arr):
            # self.assertEqual(val, 0)  # Initial values should be 0
            # arr[i] = i  # Modify the values during iteration
        # self.assertEqual(arr.get_array(), [0, 1, 2, 3, 4])  # Check if values were changed

    def test_next(self):
        """Test the __next__ method directly."""
        arr = Array(3, float)
        iterator = iter(arr)
        with self.assertRaises(StopIteration):
            next(iterator)  # Should raise StopIteration at the end

    def test_get_array(self):
        """Test retrieving the underlying array."""
        arr = Array(4, int)
        self.assertListEqual(arr.get_array(), [])

    # def test_get_item(self):

    #     arr = Array(1)
    #     self.assertEqual(arr[0], 0)

    #     with self.assertRaises(IndexError):
    #         arr = Array(0)
    #         arr[0]  # Array with no values has no index yet
    #     with self.assertRaises(IndexError):
    #         arr = Array(1)
    #         arr[1] # Array with one value has no element at position 1
    #     with self.assertRaises(IndexError):
    #         arr = Array(100)
    #         arr[50] # Array initialized with 100 elements does not yet have index 50 defined
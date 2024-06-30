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
        # self.assertEqual(arr.get_list(), [0, 1, 2, 3, 4])  # Check if values were changed

    def test_next(self):
        """Test the __next__ method directly."""
        arr = Array(3, float)
        iterator = iter(arr)
        with self.assertRaises(StopIteration):
            next(iterator)  # Should raise StopIteration at the end

    def test_get_list(self):
        """Test retrieving the underlying array."""
        arr = Array(4, int)
        self.assertListEqual(arr.get_list(), [])

    def test_add_valid_elements(self):
        """Test adding valid elements to the array."""
        arr = Array(3, int)

        # Add elements within the initial size
        arr.add(5)
        arr.add(-2)
        arr.add(10)

        self.assertEqual(arr.get_list(), [5, -2, 10])
        self.assertEqual(arr._current_size, 3)
        self.assertEqual(arr._max_size, 3)  # Size should not have changed yet

        # Add elements that trigger resizing
        arr.add(20)  # Should resize
        arr.add(30)

        self.assertEqual(arr.get_list(), [5, -2, 10, 20, 30])
        self.assertEqual(arr._current_size, 5)
        self.assertEqual(arr._max_size, 6)  # Size should have doubled

    def test_add_invalid_type(self):
        """Test adding an element of invalid type."""
        arr = Array(3, float)
        with self.assertRaises(ValueError):
            arr.add("hello")

    def test_add_to_float_array(self):
        """Test adding float elements to a float array."""
        arr = Array(2, float)
        arr.add(1.5)
        arr.add(2.7)
        self.assertEqual(arr.get_list(), [1.5, 2.7])

        # Add elements to trigger resizing
        arr.add(-3.8)
        self.assertEqual(arr.get_list(), [1.5, 2.7, -3.8])
        self.assertEqual(arr._max_size, 4)  # Size should have doubled

    def test_pop_from_non_empty_array(self):
        """Test popping elements from an array with elements."""
        sizes = [1, 5, 10]
        types = [int, float]

        for size in sizes:
            for typeof in types:
                arr = Array(size, typeof)
                for i in range(size):
                    # Add some elements
                    if typeof == float:
                        arr.add(float(i * 2))
                    else:
                        arr.add(i * 2)  

                # Pop elements and check results
                for i in reversed(range(size)):  # Pop in reverse order
                    popped_value = arr.pop()
                    self.assertEqual(popped_value, i * 2)  # Check popped value
                    self.assertEqual(arr._current_size, i)  # Check current size

    def test_pop_from_empty_array(self):
        """Test popping from an empty array (should raise IndexError)."""
        arr = Array(3, int)
        with self.assertRaises(IndexError) as context:
            arr.pop()
        self.assertEqual(str(context.exception), "Cannot pop from an empty list.")

    def test_pop_after_adding_and_removing(self):
        """Test popping after adding and removing elements."""
        arr = Array(5, float)
        for i in range(5):
            arr.add(i + 0.5)

        arr.pop()  # Remove the last element
        arr.pop()

        # Pop again and check
        popped_value = arr.pop()
        self.assertEqual(popped_value, 2.5)
        self.assertEqual(arr._current_size, 2)

    def test_multiple_pops(self):
        """Test popping multiple elements in a row."""
        arr = Array(10, int)
        for i in range(7):  # Add 7 elements
            arr.add(i)

        for _ in range(3):  # Pop 3 elements
            arr.pop()

        self.assertEqual(arr.get_list(), [0, 1, 2, 3])  # Check remaining elements

    def test_remove_existing_element(self):
        """Test removing elements that exist in the array."""
        sizes = [1, 5, 10]
        types = [int, float]

        for size in sizes:
            for typeof in types:
                arr = Array(size, typeof)
                # Create unique elements
                if typeof == float:
                    elements_to_add = [float(i * 2) for i in range(size)]
                else:
                    elements_to_add = [i * 2 for i in range(size)] 
                for element in elements_to_add:
                    arr.add(element)

                # Remove elements and check the results
                for element in elements_to_add:
                    arr.remove(element)
                    self.assertEqual(arr._current_size, len(elements_to_add) - 1)
                    self.assertNotIn(element, arr.get_list())
                    elements_to_add.remove(element)
    
    def test_remove_existing_element_wrong_type(self):
        """Test element not type of array."""
        my_array = Array(10)
        my_array.add(3)
        my_array.add(5)
        my_array.add(8)

        with self.assertRaises(ValueError):
            my_array.remove("r")

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
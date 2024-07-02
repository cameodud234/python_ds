from typing import TypeVar, Generic, Iterator
from math import isclose

T = TypeVar('T', int, float)

class Array(Generic[T]):

    _types = (int, float)
    
    def __init__(self, size: int, typeof: type[T] = int) -> None:
        """
        Creates an array with a set size.
        If items are added past the max size the 
        array will resize.
        """

        self._constructor_check(size, typeof)
        self._max_size = size
        self._current_size = 0
        self._typeof = typeof
        self._allocated_cell = [self._typeof(0)] * self._max_size

    def get_list(self) -> list[T]:
        return self._allocated_cell[:self._current_size]
    
    def get_size(self):
        return self._current_size
    
    def add(self, element: T) -> None:
        self._add_element_check(element)
        self._resize_array(element)
        self._allocated_cell[self._current_size] = element
        self._current_size += 1

    def pop(self, index: int = -1) -> T:
        """ Removes first instance of element in array """
        if index == -1:
            self._pop_element_check()
            value = self._allocated_cell[self._current_size - 1]
        else:
            self._pop_index_check(index)
            value = self._allocated_cell[index]
            for i in range(index + 1, self._current_size):
                current_index = self._current_size - 1
                while current_index != index:
                    # swap values of the current_index with the index.
                    self._allocated_cell[current_index - 1], \
                        self._allocated_cell[current_index] = self._allocated_cell[current_index], \
                            self._allocated_cell[current_index -  1]
                    current_index -= 1
        
        self._current_size -= 1
        return value
    
    def remove(self, element: T) -> None:
        """
        Removes an element at index: i and shifts all
        [i+1, n] (if starting at index) 1 values to the left by 1
        """
        self._remove_check(element)
        for i, value in enumerate(self._allocated_cell):
            if isclose(value, element):
                for j in range(i + 1, self._current_size):
                    current_index = self._current_size - 1
                    while current_index != i:
                        # swap values of the current_index with the index.
                        self._allocated_cell[current_index - 1], \
                            self._allocated_cell[current_index] = self._allocated_cell[current_index], \
                                self._allocated_cell[current_index -  1]
                        current_index -= 1
                self._current_size -= 1
                return
        raise ValueError(f"Element: {element} not found in array.")
    
    def remove_all(self, element: T) -> None:
        """
        Removes all instances of this value in the array.
        """
        pass

    def _constructor_check(self, size: int, typeof: type[T]) -> None:
        if type(size) != int:
            raise ValueError(f"Invalid size: size={size}, must be an int.")
        if size < 0:
            raise ValueError(f"Invalid size: {size}, must be greater than or equal zero.")
        if typeof not in self._types:
            raise ValueError(f"Invalid typeof: typeof={typeof}, must be int or float.")
    
    def _resize_array(self, element: T) -> None:
        if self._current_size == self._max_size:
            self._max_size *= 2
            new_arr = [self._typeof(0)] * self._max_size
            for i, element in enumerate(self._allocated_cell):
                new_arr[i] = element
            self._allocated_cell = new_arr

    def _add_element_check(self, element: T) -> None:
        if type(element) != self._typeof:
            raise ValueError(f"element: {element}, not a valid type for array of type {self._typeof}")
        
    def _pop_element_check(self) -> None:
        if self._current_size == 0:
            raise IndexError(f"Cannot pop from an empty list.")
    
    def _get_index_check(self, index: int) -> None:
        if type(index) != int:
            raise IndexError(f"Invalid index: {index}, must be an int.")
        if self._current_size == 0:
                raise IndexError(f"array: {self._allocated_cell} has no members to call upon.")
        if index < -1 or index > self._current_size:
            raise IndexError(f"Invalid index: {index}, out of list index range.")
    
    def _remove_check(self, element: T) -> None:
        if type(element) != self._typeof:
            raise ValueError(f"element: {element}, not a valid type for array of type {self._typeof}")
        return

    def _pop_index_check(self, index: int) -> None:
        if type(index) != int:
            raise(f"Invalid index: {index}, must be an int.")
        if self._current_size == 0:
                raise IndexError(f"array: {self._allocated_cell} has no members to call upon.")
        if index < -1 or index >= self._current_size:
            raise IndexError(f"Invalid index: {index}, out of list index range.")
    
    def __str__(self) -> str:
        return self._allocated_cell[:self._current_size].__str__()

    def __iter__(self) -> Iterator[T]:
        return ArrayIterator(self)
    
    def __getitem__(self, index: int) -> T:
        self._get_index_check(index)
        return self._allocated_cell[index]
    
class ArrayIterator:
    def __init__(self, array: Array):
        self._array = array
        self._current_size = 0

    def __next__(self) -> T:
        if self._current_size < self._array._current_size:
            value = self._array._allocated_cell[self._current_size]
            self._current_size += 1
            return value
        else:
            raise StopIteration
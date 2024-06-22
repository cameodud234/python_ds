from typing import Union, TypeVar
import logging

class Array:

    T = TypeVar('T', int, float)
    
    def __init__(self, size: int, typeof: type[T] = int) -> None:
        """
        Creates an array with a set size.
        If items are added past the max size the 
        array will resize.
        """

        self._types = (int, float)

        self._constructor_check(size, typeof)

        self._max_size = size
        self._current_size = 0
        self._typeof = typeof
        self._iter_position = 0
        self._allocated_cell = [self._typeof(0)] * self._max_size
        
    def _constructor_check(self, size: int, typeof: type[T]) -> None:
        if type(size) != int:
            raise ValueError(f"Invalid size: size={size}, must be an int.")
        if size < 0:
                raise ValueError(f"size: {size}, must be greater than or equal zero.")
        if typeof != int and typeof != float:
            raise ValueError(f"Invalid typeof: typeof={typeof}, must be int or float.")



    def get_array(self):
        return self._allocated_cell
    
    def __getitem__(self, index: int):
        if isinstance(index, int) and not isinstance(index, bool):

            if self._current_size == 0:
                raise IndexError(f"array: {self._allocated_cell} has no members to call upon.")
            
            if index < self._current_size and index > 0:
                return self._allocated_cell[index]
            
            else:
                raise IndexError(f"index: {index}, is out of list index range.")
    
    def __str__(self):
        return self._allocated_cell.__str__()

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter_position < self._max_size:
            value = self._allocated_cell[self._iter_position]
            self._iter_position += 1
            return value
        else:
            raise StopIteration
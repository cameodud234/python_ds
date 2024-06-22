from typing import Union, TypeVar

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
                raise ValueError(f"Invalid size: {size}, must be greater than or equal zero.")
        if typeof != int and typeof != float:
            raise ValueError(f"Invalid typeof: typeof={typeof}, must be int or float.")


    def get_array(self) -> list[type[T]]:
        return self._allocated_cell[:self._current_size]
    
    def __getitem__(self, index: int) -> type[T]:
        self._get_item_check(self, index)
        return self._allocated_cell[index]
    
    def _get_item_check(self, index: int) -> None:
        if type(index) != int:
            raise(f"Invalid index: {index}, must be an int.")
        if self._current_size == 0:
                raise IndexError(f"array: {self._allocated_cell} has no members to call upon.")
        if index < 0 or index >= self._current_size:
            raise(f"Invalid index: {index}, out of list index range.")
    
    def __str__(self) -> str:
        return self._allocated_cell.__str__()

    def __iter__(self) -> object:
        return self

    def __next__(self) -> type[T]:
        if self._iter_position < self._current_size:
            value = self._allocated_cell[self._iter_position]
            self._iter_position += 1
            return value
        else:
            raise StopIteration
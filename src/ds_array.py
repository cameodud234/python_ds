from typing import Union

class Array:

    def __init__(self, size: int, typeof: type = int) -> None:
        """
        Creates an array with a set size.
        If items are added past the max size the 
        array will resize.
        """
        if isinstance(size, int) and not isinstance(size, bool):

            if size < 0:
                raise ValueError(f"size: {size}, must be greater than or equal zero.")
            self._max_size = size
            self._current_size = 0
            self._typeof = typeof
            self._iter_position = 0

            if isinstance(typeof, type):
                if typeof == int:
                    self._allocated_cell = [0] * self._max_size

                elif typeof == float:
                    self._allocated_cell = [0.0] * self._max_size
                else:
                    raise ValueError(f"typeof value: {typeof}, must be an int or float.")
            else:
                raise ValueError(f"typeof: {type(typeof)}, must be a type.")
        else:
            raise ValueError(f"size: {size}, must be of type int.")

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

class Array:

    def __init__(self, size: int, typeof: type) -> None:
        """
        Creates an array with a set size.
        If items are added past the max size the 
        array will resize.
        """
        if isinstance(size, int) and not isinstance(size, bool):

            if size <= 0:
                raise ValueError(f"Size: {size}, must be larger than zero")
            self._max_size = size
            self._current_size = 0
            self._allocated_cell = [0] * self._max_size
            self._iter_position = 0
        else:
            raise ValueError(f"Value: {size}, of type: {type(size)}, is not an int.")

    def get_array(self):
        return self._allocated_cell
    
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
    
    # def combine_array(self, arr: iter) -> Array:
    #     """
    #     Adds values of 
    #     """

    #     accepted_types = [iter]

    #     if isinstance(arr, Array):
    #         self._allocated_cell = self._allocated_cell + arr.get_array()
    #     elif isinstance()



# class ArrayIter
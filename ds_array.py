class Array:

    def __init__(self, size: int, typeof: type) -> None:
        """
        Creates an array with a set size.
        If items are added past the max size the 
        array will resize.
        """
        if isinstance(size, int):
            if size <= 0:
                raise ValueError(f"Size: {size}, must be larger than zero")
            self._max_size = size
            self._current_size = 0
            self._allocated_cell = [0] * self._max_size
        else:
            raise ValueError(f"Value: {size}, of type: {type(size)}, is not an int.")

    def get_array(self):
        return self._allocated_cell
    
    # def combine_array(self, arr: iter) -> Array:
    #     """
    #     Adds values of 
    #     """

    #     accepted_types = [iter]

    #     if isinstance(arr, Array):
    #         self._allocated_cell = self._allocated_cell + arr.get_array()
    #     elif isinstance()
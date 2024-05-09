# Implementation of the Array2D ADT using an array of arrays.

from .array import Array


class Array2D:

    # Creates a 2-D array of size numRows x numCols
    def __init__(self, numRows, numCols):
        # Create a 1-D array to store an array reference for each row
        self._theRows = Array(numRows)

        # Create the 1-D arrays for each row of the 2-D array
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        # Returns the number of rows in the 2-D array
        return len(self._theRows)

    def numCols(self):
        # Returns the number of columns in the 2-D array
        return len(self._theRows[0])

    def clear(self, value):
        # Clears the array by setting every element to the given value
        for row in range(self.numRows()):
            row.clear(value)

    def __getitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range"
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range"
        the1dArray = self._theRows[row]
        the1dArray[col] = value

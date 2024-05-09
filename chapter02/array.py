# Implementation of the Array ADT using array capabilities of the ctypes module

import ctypes


class Array:

    def __init__(self, size):
        assert size > 0, "Array size must be greater than 0"
        self._size = size

        # Create the array structure using the ctypes module
        PyArrayType = ctypes.py_object * size
        self._items = PyArrayType()

        # Initialize each element
        self.clear(None)

    def __len__(self):
        # Returns the size of the array
        return self._size

    def __getitem__(self, idx):
        # Gets the contents of the index element
        assert idx >= 0 and idx < len(self), "Array subscript out of range"
        return self._items[idx]

    def __setitem__(self, idx, value):
        assert idx >= 0 and idx < len(self), "Array subscript out of range"
        self._items[idx] = value

    def clear(self, value):
        # Clears the array by setting each element to the given value
        for idx in range(len(self)):
            self._items[idx] = value

    def __iter__(self):
        # Returns the array's iterator for traversing the elements
        return _ArrayIterator(self._items)


# An iterator for the Array ADT

class _ArrayIterator:

    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curIdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curIdx < len(self._arrayRef):
            item = self._arrayRef[self._curIdx]
            self._curIdx += 1
            return item
        else:
            raise StopIteration
        

if __name__ == "__main__":
    array = Array(5)
    array[0] = 1
    array[1] = 2
    array[2] = 3
    array[3] = 4
    array[4] = 5
    
    for item in array:
        print(item)

    array.clear(None)
    print("After using `clear(None)` method")
    for item in array:
        print(item)
        
    
    input_txt = "qwertyuaabbrrrttttQQQiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    # create an array for the counters and initialize each element to 0
    theCounters = Array(127)
    theCounters.clear(0)

    for ch in input_txt:
        code = ord(ch)
        theCounters[code] += 1


    for i in range(26):
        print("%c - %4d     %c - %4d" % (chr(65 + i), theCounters[65+i], chr(97+i), theCounters[97+i]))
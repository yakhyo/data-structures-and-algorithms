# Implementation of the Bag ADT container using a Python list

class Bag:

    def __init__(self):
        # Constructs an empty bag
        self._theItems = list()

    def __len__(self):
        # Returns the number of items in the bag
        return len(self._theItems)

    def __contains__(self, item):
        # Determines if an item is contained in the bag
        return item in self._theItems

    def add(self, item):
        # Adds a new item to the bag
        self._theItems.append(item)

    def remove(self, item):
        # Removes and returns an instance of the item from the bag
        assert item in self._theItems, "The item is not in the bag"
        idx = self._theItems.index(item)
        return self._theItems.pop(idx)

    def __iter__(self):
        # Return an iterator for traversing the list of items
        return _BagIterator(self._theItems)


# An iterator for the Bag ADT

class _BagIterator:

    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration


if __name__ == "__main__":
    # Create Bag instance
    bag = Bag()

    # Add items
    bag.add(1)
    bag.add(2)
    bag.add(3)
    bag.add(4)
    bag.add(5)

    # Iterate over the bag items
    for item in bag:
        print(item)

    # Length of the bag
    print("Length:", len(bag))

    # Contains
    print("Contains:", 6 in bag)

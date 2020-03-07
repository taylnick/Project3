from proj3 import *

class unsorted_array(list):
    def __init__(self, dist, src):
        super().__init__()
        self.size = len(dist)
        self.decrease_key(src, 0)

    def is_empty(self):
        return self.size == 0

    def insert(self, node, **kwargs):
        pass

# Returns node with min value freshly set to None
    def delete_min(self):
        id = None
        min = float("inf")
        for index, value in enumerate(self):
            if (value is not None) and (value < min):
                id = index
                min = value
        self.decrease_key(id, None)
        return self[id]

    def decrease_key(self, index, value):
        self[index] = value

# Binary Heap class operations
class binary_heap:
    def __init__(self, dist, src):
        self.size = len(dist)

    def is_empty(self):
        return self.size == 0

    def insert(self, node):
        pass

    def delete_min(self):
        pass

    def decrease_key(self):
        pass
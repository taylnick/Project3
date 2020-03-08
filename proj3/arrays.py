from proj3.CS4412Graph import *
from proj3.NetworkRoutingSolver import *


class unsorted_array:
    def __init__(self, dist, src):
        self.size = len(dist)
        self.array = []
        for i in range(self.size):
            self.array.append(dist[i])
        self.decrease_key(src, 0)

    def is_empty(self):
        return self.size == 0

    def insert(self, node):
        self.array.append(node)
        self.size += 1
        pass

    # Returns node with min value freshly set to None
    def delete_min(self):
        min_id = None
        min_value = float("inf")
        for index, value in enumerate(self.array):
            if (value is not None) and (value < min_value):
                min_id = index
                min_value = value
        self.decrease_key(min_id, None)
        self.size -= 1
        return min_id

    def decrease_key(self, index, value):
        self.array[index] = value


# Binary Heap class operations
class binary_heap:

    def __init__(self, dist, src):
        self.heapList = [0]
        self.size = 0
        self.point_arr = [-1] * len(dist)

        for i in range(len(dist)):
            self.insert(i, dist[i])
        self.decrease_key(src, 0)

    def is_empty(self):
        return self.size == 0

    def still_contains(self, i):
        pos = self.point_arr[i]
        if pos is None:
            return False
        else:
            return pos <= self.size

    def insert(self, i, val):
        self.heapList.append(val)
        self.size += 1
        self.point_arr[i] = self.size
        self.percolate_up(i)

# Should return the index of the node removed.
    def delete_min(self):
        to_delete = self.point_arr.index(1)
        node_id = self.point_arr.index(1)
        self.point_arr[node_id] = None
        if self.size == 1:
            self.heapList.pop()
            self.size -= 1
            return to_delete

        self.heapList[1] = self.heapList[self.size]
        new_top = self.point_arr.index(self.size)
        self.point_arr[new_top] = 1
        self.size -= 1
        self.heapList.pop()
        self.percolate_down(new_top)
        return to_delete

    def decrease_key(self, i, value):
        pos = self.point_arr[i]
        self.heapList[pos] = value
        self.percolate_up(i)

    def percolate_up(self, node_id):
        pos = self.point_arr[node_id]
        # while there is a parent
        while pos // 2 > 0:
            # if the child is weighted less than the parent
            if self.heapList[pos] < self.heapList[pos // 2]:
                # Swap weights in the tree
                temp = self.heapList[pos // 2]
                self.heapList[pos // 2] = self.heapList[pos]
                self.heapList[pos] = temp
                # Swap the position value of the two nodes.
                swap_node = self.point_arr.index(pos // 2)
                self.point_arr[node_id] = pos // 2
                self.point_arr[swap_node] = pos
            pos = pos // 2

    def percolate_down(self, node_id):
        pos = self.point_arr[node_id]
        while (pos * 2) <= self.size:
            min_pos = self.min_child(pos)
            # if the parent is larger than its smallest child
            if self.heapList[pos] > self.heapList[min_pos]:
                # Swap the parent and child
                temp = self.heapList[pos]
                self.heapList[pos] = self.heapList[min_pos]
                self.heapList[min_pos] = temp
                # Swap the values in pointer_arr too
                swap_node = self.point_arr.index(min_pos)
                self.point_arr[node_id] = min_pos
                self.point_arr[swap_node] = pos
            pos = min_pos

    def min_child(self, i):
        if (i * 2 + 1) > self.size:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

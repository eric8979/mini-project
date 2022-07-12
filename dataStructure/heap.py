# Heap is represented using list/array

# min-Heap
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # T: O(n)
    def buildHeap(self, array):
        # build heap using siftDown() (can use siftUp() too)
        # lowestParentIdx = (len(array) - 1) // 2
        # from lowestParentIdx to idx=0 are all parents
        return None

    # T: O(log(n)) at most / S: O(1)
    def siftDown(self, newIdx, heap):
        # Order node from top to bottom 
        # Used for removing
        return None

    # T: O(log(n)) / S: O(1)
    def siftUp(self, newIdx):
        # Order node from bottom to top
        # Used for inserting
        return None

    def remove(self):
        # remove "root" node
        # Swap root and last node
        # pop() last node
        # siftDown() new root node
        return None

    def insert(self, value):
        # insert value at the bottom
        # siftUp() to order
        return None

# --------------------

# Using heapq (not actually creating the structure)
import heapq

list = [4,2,6,3,8,9]
heapq.heapify(list)
print(list)


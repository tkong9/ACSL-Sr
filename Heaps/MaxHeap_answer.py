"""
Max Heap

Name: <Your Name>
"""

"""
Max Heap is a data structure that supports the following operations:
    - insert: insert an element into the heap
    - extract_max: extract the maximum element from the heap

The heap is represented as an array. The root of the heap is at index 1.
The left child of the node at index i is at index 2i.
The right child of the node at index i is at index 2i + 1.

The heap property is that the value of a node is greater than or equal to
the values of its children.

For example, the following array represents a max heap:
    [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

The following array does not represent a max heap:
    [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 11]


Time Complexity:
    - insert: O(log n)
    - extract_max: O(log n)

Space Complexity:
    - O(n)
"""


class MaxHeap:
    """Implements a max heap data structure"""

    def __init__(self):
        """Initialize the heap with a dummy element at index 0"""
        self.heap = [0]

    def insert(self, val):
        """
        Insert an element into the heap

        Args:
            val: The value to be inserted
        """
        # TODO: Implement this method
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """
        Extract the maximum element from the heap
        Remove the maximum element from the heap and return it

        Returns:
            The maximum element from the heap. If the heap is empty, returns None.
        """
        # TODO: Implement this method
        if len(self.heap) == 1:
            return None

        max_val = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        self._heapify_down(1)
        return max_val

    # Below are helper methods for the MaxHeap class. You do not have to use them, but I recommend doing so to
    # simplify your code. If you choose not to use them, you may delete them.
    def _parent(self, index):
        """Return the index of the parent of the node at index"""
        # TODO: Implement this method
        return index // 2

    def _left_child(self, index):
        """Return the index of the left child of the node at index"""
        # TODO: Implement this method
        return 2 * index

    def _right_child(self, index):
        """Return the index of the right child of the node at index"""
        # TODO: Implement this method
        return 2 * index + 1

    def _swap(self, i, j):
        """Swap the elements at indices i and j"""
        # TODO: Implement this method
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        """
        Bubble up the element at index to its proper place

        Args:
            index: The index of the element to bubble up
        """
        # TODO: Implement this method
        while index > 1 and self.heap[index] > self.heap[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _heapify_down(self, index):
        """
        Bubble down the element at index to its proper place

        Args:
            index: The index of the element to bubble down
        """
        # TODO: Implement this method
        max_index = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left

        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right

        if index != max_index:
            self._swap(index, max_index)
            self._heapify_down(max_index)


def test_max_heap_simple():
    print('Testing simple Max Heap...', end='')
    heap = MaxHeap()

    # Test inserting elements
    heap.insert(10)
    assert heap.heap[1] == 10

    heap.insert(20)
    assert heap.heap[1] == 20
    assert heap.heap[2] == 10

    heap.insert(15)
    assert heap.heap[1] == 20
    assert heap.heap[2] == 10
    assert heap.heap[3] == 15

    # Test extracting max element
    assert heap.extract_max() == 20
    assert heap.heap[1] == 15
    assert heap.heap[2] == 10

    assert heap.extract_max() == 15
    assert heap.heap[1] == 10

    assert heap.extract_max() == 10
    assert len(heap.heap) == 1  # Only the dummy element should remain

    # Test extracting from an empty heap
    assert heap.extract_max() is None
    print('Passed!')


def test_max_heap_complex():
    print('Testing complex Max Heap...', end='')
    heap = MaxHeap()

    # Test empty heap
    assert heap.extract_max() is None

    # Insert single element
    heap.insert(5)
    assert heap.extract_max() == 5
    assert heap.extract_max() is None

    # Insert multiple elements
    for i in range(1, 11):
        heap.insert(i)

    # Extract elements and verify max order
    for i in range(10, 0, -1):
        assert heap.extract_max() == i

    # Test with duplicates
    heap.insert(5)
    heap.insert(5)
    heap.insert(3)
    heap.insert(3)

    assert heap.extract_max() == 5
    assert heap.extract_max() == 5
    assert heap.extract_max() == 3
    assert heap.extract_max() == 3
    assert heap.extract_max() is None

    # Test with negative numbers
    heap.insert(-5)
    heap.insert(-3)
    heap.insert(-7)

    assert heap.extract_max() == -3
    assert heap.extract_max() == -5
    assert heap.extract_max() == -7
    assert heap.extract_max() is None

    # Test with mixed positive and negative numbers
    heap.insert(-5)
    heap.insert(3)
    heap.insert(-7)
    heap.insert(6)

    assert heap.extract_max() == 6
    assert heap.extract_max() == 3
    assert heap.extract_max() == -5
    assert heap.extract_max() == -7
    assert heap.extract_max() is None
    print('Passed!')


if __name__ == "__main__":
    test_max_heap_simple()
    test_max_heap_complex()

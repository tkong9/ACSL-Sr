"""
Min Heap

Name: <Your Name>
"""

"""
Min Heap is a data structure that supports the following operations:
    - insert: insert an element into the heap
    - extract_min: extract the minimum element from the heap

The heap is represented as an array. The root of the heap is at index 1.
The left child of the node at index i is at index 2i.
The right child of the node at index i is at index 2i + 1.

The heap property is that the value of a node is less than or equal to
the values of its children.

For example, the following array represents a min heap:
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Time Complexity:
    - insert: O(log n)
    - extract_min: O(log n)

Space Complexity:
    - O(n)
"""


class MinHeap:
    """Implements a min heap data structure"""

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
        pass

    def extract_min(self):
        """
        Extract the minimum element from the heap

        Returns:
            The minimum element from the heap. If the heap is empty, returns None.
        """
        # TODO: Implement this method
        pass

    # Below are helper methods for the MaxHeap class. You do not have to use them, but I recommend doing so to
    # simplify your code. If you choose not to use them, you may delete them.
    def _parent(self, index):
        """Return the index of the parent of the node at index"""
        # TODO: Implement this method
        pass

    def _left_child(self, index):
        """Return the index of the left child of the node at index"""
        # TODO: Implement this method
        pass

    def _right_child(self, index):
        """Return the index of the right child of the node at index"""
        # TODO: Implement this method
        pass

    def _swap(self, i, j):
        """Swap the elements at indices i and j"""
        # TODO: Implement this method
        pass

    def _heapify_up(self, index):
        """
        Bubble up the element at index to its proper place

        Args:
            index: The index of the element to bubble up
        """
        # TODO: Implement this method
        pass

    def _heapify_down(self, index):
        # TODO: Implement this method
        """
        Bubble down the element at index to its proper place

        Args:
            index: The index of the element to bubble down
        """
        pass


def test_min_heap_simple():
    print('Testing simple MinHeap...', end='')
    heap = MinHeap()

    # Test inserting elements
    heap.insert(10)
    assert heap.heap[1] == 10

    heap.insert(20)
    assert heap.heap[1] == 10
    assert heap.heap[2] == 20

    heap.insert(5)
    assert heap.heap[1] == 5
    assert heap.heap[2] == 20
    assert heap.heap[3] == 10

    # Test extracting min element
    assert heap.extract_min() == 5
    assert heap.heap[1] == 10
    assert heap.heap[2] == 20

    assert heap.extract_min() == 10
    assert heap.heap[1] == 20

    assert heap.extract_min() == 20
    assert len(heap.heap) == 1  # Only the dummy element should remain

    # Test extracting from an empty heap
    assert heap.extract_min() is None
    print('Passed!')


def test_min_heap_complex():
    print('Testing complex MinHeap...', end='')
    heap = MinHeap()

    # Test empty heap
    assert heap.extract_min() is None

    # Insert single element
    heap.insert(5)
    assert heap.extract_min() == 5
    assert heap.extract_min() is None

    # Insert multiple elements
    for i in range(10, 0, -1):
        heap.insert(i)

    # Extract elements and verify min order
    for i in range(1, 11):
        assert heap.extract_min() == i

    # Test with duplicates
    heap.insert(5)
    heap.insert(5)
    heap.insert(3)
    heap.insert(3)

    assert heap.extract_min() == 3
    assert heap.extract_min() == 3
    assert heap.extract_min() == 5
    assert heap.extract_min() == 5
    assert heap.extract_min() is None

    # Test with negative numbers
    heap.insert(-5)
    heap.insert(-3)
    heap.insert(-7)

    assert heap.extract_min() == -7
    assert heap.extract_min() == -5
    assert heap.extract_min() == -3
    assert heap.extract_min() is None

    # Test with mixed positive and negative numbers
    heap.insert(-5)
    heap.insert(3)
    heap.insert(-7)
    heap.insert(6)

    assert heap.extract_min() == -7
    assert heap.extract_min() == -5
    assert heap.extract_min() == 3
    assert heap.extract_min() == 6
    assert heap.extract_min() is None
    print('Passed!')


if __name__ == '__main__':
    test_min_heap_simple()
    test_min_heap_complex()

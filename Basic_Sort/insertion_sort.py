"""
Insertion Sort

Name: <your name>
"""

"""
Insertion sort is a simple sorting algorithm that builds the final sorted list one item at a time.
Insertion sort has the following steps:
    1. Start from the second element in the list.
    2. Compare the current element with the previous element.
    3. If the current element is less than the previous element, swap them.
    4. If the current element is greater than or equal to the previous element, move to the next element.
    5. Repeat steps 2-4 until the beginning of the list is reached.
    6. Repeat steps 1-5 until the list is sorted.

Insertion sort has a time complexity of O(n^2) where n is the number of elements in the list.
Insertion sort has a space complexity of O(1) because it does not use any additional space.

Complete the 'insertion_sort' function below.
"""


def insertion_sort(lst):
    """
    Perform the insertion sort algorithm on a list.

    :param lst: List of unordered elements
    :return: Sorted list of elements

    Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.
    It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
    However, insertion sort provides several advantages:
    - Simple implementation
    - Efficient for (quite) small data sets, much like other quadratic sorting algorithms
    - More efficient in practice than most other simple quadratic (i.e., O(n^2)) algorithms such as selection sort or bubble sort
    - Adaptive, i.e., efficient for data sets that are already substantially sorted
    """
    # TODO: Write your code here
    pass


def test_insertion_sort():
    print('Testing insertion_sort()...', end='')
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert insertion_sort([1, 2]) == [1, 2]
    assert insertion_sort([2, 1]) == [1, 2]
    assert insertion_sort([3, 2, 1]) == [1, 2, 3]
    assert insertion_sort([1, 3, 2]) == [1, 2, 3]
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert insertion_sort([3, 5, 8, 2, 9, 3, 0]) == [0, 2, 3, 3, 5, 8, 9]
    assert insertion_sort([3, 5, 8, -30, 2, 9, 3, 0, 1, -3, -2, -5]) == [-30, -5, -3, -2, 0, 1, 2, 3, 3, 5, 8, 9]
    print('Passed.')


if __name__ == '__main__':
    test_insertion_sort()

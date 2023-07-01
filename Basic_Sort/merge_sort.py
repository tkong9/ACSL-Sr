"""
Merge Sort

Name: <your name>
"""

"""
Merge sort is a sorting algorithm that uses the divide and conquer approach.
Merge sort has the following steps:
    1. Divide the list into two halves.
    2. Sort each half recursively.
    3. Merge the two sorted halves.

Merge sort has a time complexity of O(n log n) where n is the number of elements in the list.
Merge sort has a space complexity of O(n) because it uses additional space to store the two halves of the list.

Complete the 'merge_sort' function below.
"""


def merge_sort(lst):
    """
    Perform the merge sort algorithm on a list.

    :param lst: List of unordered elements
    :return: Sorted list of elements

    Merge sort is a divide-and-conquer algorithm that works by recursively breaking down
    a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly.
    The solutions to the sub-problems are then combined to give a solution to the original problem.
    """
    # TODO: Implement merge sort
    pass


def merge(left_list, right_list):
    """
    Merge two lists in a sorted manner.

    :param left_list: Sorted list of elements
    :param right_list: Sorted list of elements
    :return: Single sorted list combined from left_list and right_list

    This function assumes that `left_list` and `right_list` are sorted and merges them
    into a single sorted list in linear time.
    """
    # TODO: Implement merge
    pass


def test_merge_sort():
    print('Testing merge_sort()...', end='')
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([1, 2]) == [1, 2]
    assert merge_sort([2, 1]) == [1, 2]
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([1, 3, 2]) == [1, 2, 3]
    assert merge_sort([1, 2, 3]) == [1, 2, 3]
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([3, 5, 8, 2, 9, 3, 0]) == [0, 2, 3, 3, 5, 8, 9]
    assert merge_sort([3, 5, 8, -30, 2, 9, 3, 0, 1, -3, -2, -5]) == [-30, -5, -3, -2, 0, 1, 2, 3, 3, 5, 8, 9]
    print('Passed.')


if __name__ == '__main__':
    test_merge_sort()

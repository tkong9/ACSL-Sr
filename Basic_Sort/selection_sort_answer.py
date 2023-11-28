"""
Selection Sort

Name: <your name>
"""

"""
Selection sort is a simple sorting algorithm that repeatedly finds the minimum element from the unsorted part of the list and puts it at the beginning.
Selection sort has the following steps:
    1. Find the minimum element in the unsorted part of the list.
    2. Swap the minimum element with the first element in the unsorted part of the list.
    3. Repeat steps 1-2 until the list is sorted.
    
Selection sort has a time complexity of O(n^2) where n is the number of elements in the list.
Selection sort has a space complexity of O(1) because it does not use any additional space.

Complete the 'selection_sort' function below.
"""


def selection_sort(lst):
    """
    Perform the selection sort algorithm on a list.

    :param lst: List of unordered elements
    :return: Sorted list of elements

    Selection sort is a simple comparison-based algorithm. It seeks out the smallest element in the list and
    swaps it with the first element. It then finds the smallest element in the rest of the list and swaps
    it with the second element, and so on. In other words, after the i-th pass, the i smallest items are in place.

    This sort is noted for its simplicity and also has performance advantages over more complicated
    algorithms in certain situations, particularly where auxiliary memory is limited.
    """
    # TODO: Write your code here
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


def test_selection_sort():
    print('Testing selection_sort()...', end='')
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([1, 2]) == [1, 2]
    assert selection_sort([2, 1]) == [1, 2]
    assert selection_sort([3, 2, 1]) == [1, 2, 3]
    assert selection_sort([1, 3, 2]) == [1, 2, 3]
    assert selection_sort([1, 2, 3]) == [1, 2, 3]
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert selection_sort([3, 5, 8, 2, 9, 3, 0]) == [0, 2, 3, 3, 5, 8, 9]
    assert selection_sort([3, 5, 8, -30, 2, 9, 3, 0, 1, -3, -2, -5]) == [-30, -5, -3, -2, 0, 1, 2, 3, 3, 5, 8, 9]
    print('Passed.')


if __name__ == '__main__':
    test_selection_sort()

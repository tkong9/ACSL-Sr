"""
Bubble Sort

Name: <your name>
"""

"""
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
Bubble sort has the following steps:
    1. Start from the first element in the list.
    2. Compare the current element with the next element.
    3. If the current element is greater than the next element, swap them.
    4. If the current element is less than or equal to the next element, move to the next element.
    5. Repeat steps 2-4 until the end of the list is reached.
    6. Repeat steps 1-5 until the list is sorted.

Bubble sort has a time complexity of O(n^2) where n is the number of elements in the list.
Bubble sort has a space complexity of O(1) because it does not use any additional space.

Complete the 'bubble_sort' function below.
"""


def bubble_sort(lst):
    """
    Perform the bubble sort algorithm on a list.

    :param lst: List of unordered elements
    :return: Sorted list of elements

    Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they are in the wrong order.
    The pass through the list is repeated until the list is sorted.
    """
    # TODO: Write your code here
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def test_bubble_sort():
    print('Testing bubble_sort()...', end='')
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([1, 2]) == [1, 2]
    assert bubble_sort([2, 1]) == [1, 2]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([1, 3, 2]) == [1, 2, 3]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([3, 5, 8, 2, 9, 3, 0]) == [0, 2, 3, 3, 5, 8, 9]
    assert bubble_sort([3, 5, 8, -30, 2, 9, 3, 0, 1, -3, -2, -5]) == [-30, -5, -3, -2, 0, 1, 2, 3, 3, 5, 8, 9]
    print('Passed.')


if __name__ == '__main__':
    # test_bubble_sort()
    nums = [3, 5, 8, -30, 2, 9, 3, 0, 1, -3, -2, -5]
    bubble_sort(nums)
    print(nums)

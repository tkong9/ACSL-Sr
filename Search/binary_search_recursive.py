"""
Binary Search Recursive

Name: <your name>
"""

"""
Binary Search is a searching algorithm that searches for an item in a sorted list by repeatedly dividing the list in half
and searching for the item in the half where the item might be located.

Binary Search has the following steps:
    1. Start from the middle item in the list.
    2. Compare the item with the item we are searching for.
    3. If the item is found, return the index of the item.
    4. If the item is not found, check if the item is less than or greater than the middle item.
    5. If the item is less than the middle item, repeat steps 1-4 with the left half of the list.
    6. If the item is greater than the middle item, repeat steps 1-4 with the right half of the list.
    7. Repeat steps 1-6 until the item is found or the end of the list is reached.
    8. If the item is not found, return -1.

Binary Search has a time complexity of O(log n) where n is the number of items in the list.
Binary Search (recursive) has a space complexity of O(log n) because it uses additional space for the recursive calls.

Complete the 'binary_search_recursive' function below.
"""


def binary_search_recursive(lst, target, low=0, high=None):
    """
    Perform a binary search on a sorted list.

    This function recursively divides the list in half until the target value is found or the search space is exhausted.
    If a match is found, the index of the matching element is returned. If no match is found, -1 is returned.

    Parameters:
    lst (list): The sorted list to be searched.
    target (any): The value to be searched for.
    low (int, optional): The lower bound of the search space. Defaults to 0.
    high (int, optional): The upper bound of the search space. Defaults to the length of the list minus 1.

    Returns:
    int: The index of the target value if it exists in the list, else -1.
    """
    # TODO: Implement the binary search algorithm recursively here
    pass


def test_binary_search_recursive():
    print('Testing binary_search_recursive()...', end='')
    numbers = [1, 2, 3, 4, 5]
    assert binary_search_recursive(numbers, 3) == 2
    assert binary_search_recursive(numbers, 6) == -1
    numbers2 = [3, 6, 9, 12, 15, 47, 57, 68, 72, 84, 89, 91, 95, 99]
    assert binary_search_recursive(numbers2, 95) == 12
    assert binary_search_recursive(numbers2, 100) == -1
    assert binary_search_recursive(numbers2, 3) == 0
    assert binary_search_recursive(numbers2, 99) == 13
    assert binary_search_recursive(numbers2, 47) == 5
    assert binary_search_recursive(numbers2, 0) == -1
    print('Passed!')


if __name__ == '__main__':
    test_binary_search_recursive()

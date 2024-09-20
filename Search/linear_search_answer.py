"""
Linear Search

Name: <your name>
"""

"""
Linear Search is a searching algorithm that searches for an item in a list by going through each item in the list
starting from the first item until the item is found or the end of the list is reached.

Linear Search has the following steps:
    1. Start from the first item in the list.
    2. Compare the item with the item we are searching for.
    3. If the item is found, return the index of the item.
    4. If the item is not found, move to the next item in the list.
    5. Repeat steps 2-4 until the item is found or the end of the list is reached.
    6. If the item is not found, return -1.
    
Linear Search has a time complexity of O(n) where n is the number of items in the list.
Linear Search has a space complexity of O(1) because it does not use any additional space.

Complete the 'linear_search' function below.
"""


def linear_search(lst, target):
    """
    Perform a linear search on a list.

    This function iteratively checks each element of the list to see if it is equal to the target value.
    If a match is found, the index of the matching element is returned. If no match is found, -1 is returned.

    Parameters:
    lst (list): The list to be searched.
    target (any): The value to be searched for.

    Returns:
    int: The index of the target value if it exists in the list, else -1.
    """
    # TODO: Write your code here
    for i in range(len(lst)):
        if lst[i] == target:
            return i  # return the index of the matching element

    return -1  # return -1 if no match is found


def test_linear_search():
    print('Testing linear_search()...', end='')
    numbers = [1, 2, 3, 4, 5]
    assert linear_search(numbers, 3) == 2
    assert linear_search(numbers, 6) == -1
    assert linear_search(numbers, 1) == 0
    assert linear_search(numbers, 5) == 4
    assert linear_search(numbers, 2) == 1
    assert linear_search(numbers, 4) == 3
    numbers2 = [34, 6, 8, 2, 4, 45, 78, 3, 86, 7]
    assert linear_search(numbers2, 45) == 5
    assert linear_search(numbers2, 86) == 8
    assert linear_search(numbers2, 7) == 9
    assert linear_search(numbers2, -23) == -1
    assert linear_search(numbers2, 1000) == -1
    print('Passed.')


if __name__ == '__main__':
    test_linear_search()

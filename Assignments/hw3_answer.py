"""
hw3

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
            return i
    return -1


def triangle_number(n):
    """
    Compute the nth triangular number.

    This function uses a recursive approach to compute the nth triangular number.
    A triangular number counts the objects that can form an equilateral triangle.
    The nth triangular number is the number of dots composing a triangle with n dots on a side,
    and it represents the sum of the n natural numbers from 1 to n.
    Visualize Triangle Number: https://www.mathsisfun.com/algebra/triangular-numbers.html

    Parameters:
    n (int): The number to compute the triangular number of.

    Returns:
    int: The nth triangular number.
    """
    # TODO: Write your code here
    if n == 1:
        return 1
    return n + triangle_number(n-1)


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
Binary Search (iterative) has a space complexity of O(1) because it does not use any additional space.
Binary Search (recursive) has a space complexity of O(log n) because it uses additional space for the recursive calls.

Complete the 'binary_search_iterative' function below.
"""
def binary_search_iterative(lst, target):
    """
    Perform an iterative binary search on a sorted list.

    This function repeatedly divides the search space in half until the target value is found or the search space is exhausted.
    If a match is found, the index of the matching element is returned. If no match is found, -1 is returned.

    Parameters:
    lst (list): The sorted list to be searched.
    target (any): The value to be searched for.

    Returns:
    int: The index of the target value if it exists in the list, else -1.
    """
    # TODO: Implement the binary search algorithm iteratively here
    low, high = 0, len(lst) - 1

    while low <= high:
        mid = (low + high) // 2  # find the midpoint
        if lst[mid] == target:
            return mid  # the target value is found
        elif lst[mid] > target:
            high = mid - 1  # continue to search in the left half
        else:
            low = mid + 1  # continue to search in the right half

    return -1  # the search space is exhausted, and the target is not found



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
    if high is None:
        high = len(lst) - 1

    if low > high:
        return -1  # the search space is exhausted, and the target is not found

    mid = (low + high) // 2  # find the midpoint

    if lst[mid] == target:
        return mid  # the target value is found
    elif lst[mid] > target:
        return binary_search_recursive(lst, target, low, mid-1)  # search in the left half
    else:
        return binary_search_recursive(lst, target, mid+1, high)  # search in the right half



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
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


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
    if len(lst) <= 1:
        return lst

    # divide list into two halves
    mid = len(lst) // 2
    left_list = merge_sort(lst[:mid]) # recursive call
    right_list = merge_sort(lst[mid:]) # recursive call

    return merge(left_list, right_list)


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
    sorted_list = []
    left_list_index = right_list_index = 0

    # Merge small elements first
    while left_list_index < len(left_list) and right_list_index < len(right_list):
        if left_list[left_list_index] <= right_list[right_list_index]:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
        else:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

    # If left_list has more items, add them to sorted_list
    while left_list_index < len(left_list):
        sorted_list.append(left_list[left_list_index])
        left_list_index += 1

    # If right_list has more items, add them to sorted_list
    while right_list_index < len(right_list):
        sorted_list.append(right_list[right_list_index])
        right_list_index += 1

    return sorted_list




"""
Test Cases ----------------------------------------------------------------------
"""
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


def test_binary_search_iterative():
    print('Testing binary_search_iterative()...', end='')
    numbers = [1, 2, 3, 4, 5]
    assert binary_search_iterative(numbers, 3) == 2
    assert binary_search_iterative(numbers, 6) == -1
    numbers2 = [3, 6, 9, 12, 15, 47, 57, 68, 72, 84, 89, 91, 95, 99]
    assert binary_search_iterative(numbers2, 95) == 12
    assert binary_search_iterative(numbers2, 100) == -1
    assert binary_search_iterative(numbers2, 3) == 0
    assert binary_search_iterative(numbers2, 99) == 13
    assert binary_search_iterative(numbers2, 47) == 5
    assert binary_search_iterative(numbers2, 0) == -1
    print('Passed!')


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


def test_triangle_number():
    print('Testing triangle_number()...', end='')
    assert triangle_number(1) == 1
    assert triangle_number(2) == 3
    assert triangle_number(3) == 6
    assert triangle_number(4) == 10
    assert triangle_number(5) == 15
    assert triangle_number(6) == 21
    assert triangle_number(7) == 28
    assert triangle_number(8) == 36
    assert triangle_number(9) == 45
    assert triangle_number(10) == 55
    assert triangle_number(11) == 66
    assert triangle_number(12) == 78
    assert triangle_number(13) == 91
    assert triangle_number(14) == 105
    assert triangle_number(15) == 120
    assert triangle_number(16) == 136
    assert triangle_number(17) == 153
    assert triangle_number(18) == 171
    assert triangle_number(19) == 190
    assert triangle_number(20) == 210
    assert triangle_number(21) == 231
    assert triangle_number(22) == 253
    assert triangle_number(23) == 276
    assert triangle_number(24) == 300
    assert triangle_number(25) == 325
    assert triangle_number(26) == 351
    assert triangle_number(27) == 378
    assert triangle_number(28) == 406
    assert triangle_number(29) == 435
    assert triangle_number(30) == 465
    assert triangle_number(31) == 496
    assert triangle_number(32) == 528
    assert triangle_number(33) == 561
    assert triangle_number(34) == 595
    assert triangle_number(35) == 630
    assert triangle_number(36) == 666
    assert triangle_number(37) == 703
    assert triangle_number(38) == 741
    assert triangle_number(39) == 780
    assert triangle_number(40) == 820
    assert triangle_number(41) == 861
    assert triangle_number(42) == 903
    assert triangle_number(43) == 946
    assert triangle_number(44) == 990
    print("All test cases passed!")


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


def test_all():
    test_linear_search()
    test_triangle_number()
    test_binary_search_iterative()
    test_binary_search_recursive()
    test_bubble_sort()
    test_selection_sort()
    test_insertion_sort()
    test_merge_sort()


if __name__ == '__main__':
    test_all()

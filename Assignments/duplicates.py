class TreeNode:
    def __init__(self, value):
        """Initialize a TreeNode with a given value."""
        self.value = value
        self.count = 1
        self.left = None
        self.right = None


def insert(root, value):
    """
    Insert a value into the binary search tree rooted at 'root'.

    Args:
    - root (TreeNode): The root of the binary search tree.
    - value (str): The value to be inserted.

    Returns:
    - TreeNode: The root of the modified tree.
    """
    if not root:
        return TreeNode(value)

    if value == root.value:
        root.count += 1
    elif value <= root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def sum_single_child_nodes(root):
    """
    Calculate the sum of counts for nodes with a single child in the binary search tree rooted at 'root'.

    Args:
    - root (TreeNode): The root of the binary search tree.

    Returns:
    - int: The sum of counts for nodes with a single child.
    """
    if not root:
        return 0

    # Check if the node has a single child
    if bool(root.left) != bool(root.right):
        return root.count + sum_single_child_nodes(root.left) + sum_single_child_nodes(root.right)

    return sum_single_child_nodes(root.left) + sum_single_child_nodes(root.right)


def process_string(s):
    """
    Process the input string, build a binary search tree, and calculate the desired output.

    Args:
    - s (str): The input string.

    Returns:
    - int: The sum of counts for nodes with a single child in the constructed tree.
    """
    # Filter out non-letters and convert to uppercase
    s = ''.join(filter(str.isalpha, s)).upper()

    root = None
    for char in s:
        root = insert(root, char)

    return sum_single_child_nodes(root)


def test1():
    test_strings = [
        "abracadabracabob",
        "American Computer Science League",
        "Python and Java are programming languages",
        "Python and Java and java and python",
        "the quick brown fox jumped over the lazy river"
    ]

    expected_outputs = [15, 9, 23, 18, 9]

    print('Running a first test set...')
    for idx, (test_str, expected) in enumerate(zip(test_strings, expected_outputs), 1):
        result = process_string(test_str)
        assert result == expected, f"Test {idx} failed. Expected {expected}, but got {result}."
        print(f"Test {idx} passed!")
    print('All tests passed!')


def test2():
    print('Running a second test set...')
    test_strings = [
        "simple simon",
        "simple simon simply said something slowly",
        "peter piper picked a peck of pickles",
        "peter piper picked a peck of pickled peppers",
        "how much wood could a woodchuck chuck if a woodchuck could chuck wood"
    ]

    expected_outputs = [4, 10, 7, 8, 18]

    for idx, (test_str, expected) in enumerate(zip(test_strings, expected_outputs), 1):
        result = process_string(test_str)
        assert result == expected, f"Test {idx} failed. Expected {expected}, but got {result}."
        print(f"Test {idx} passed!")
    print('All tests passed!')


if __name__ == "__main__":
    test1()
    print()
    test2()

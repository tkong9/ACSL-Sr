"""
Name: Yun Woo Lee
"""
import re


class newNode:
    """
    A class that manages the properties of a node in a
    Binary Search Tree.
    """

    def __init__(self, data):
        self.key = data
        self.count = 1
        self.left = None
        self.right = None


def insert(node, key):
    """
    A function that inserts a new node with given key in BST.
    If a tree is empty, a new node is returned.
    If a key already exists in BST, it increments the count of the existing node.
    """

    if node == None:
        k = newNode(key)
        return k

    if key == node.key:
        (node.count) += 1
        return node

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def printNodesOneChild(root, single_child_nodes):
    # Checks if a node have only one child, then traverses to the next node and performs the same check.
    if not root:
        return

    if not root.left and root.right:
        single_child_nodes.append(root)
    elif root.left and not root.right:
        single_child_nodes.append(root)

    printNodesOneChild(root.left, single_child_nodes)

    printNodesOneChild(root.right, single_child_nodes)
    return


def process_string(s):
    """
    The function processes the string by making it all upper case.
    Then, the function inserts each characters of the string into the BST.
    After that, it gets the nodes that only have one child.
    Finally, the function adds up all the counts in each node and outputs the
    total value.

    Args:
    - s (str): The input string.

    Returns:
    - int: The sum of counts for nodes with a single child in the constructed tree.
    """
    single_child_nodes = []
    s = s.upper()
    s = re.sub('[\W_]+', '', s)
    root = None
    i = 0
    while i < len(s):
        root = insert(root, s[i])
        i = i + 1
    printNodesOneChild(root, single_child_nodes)
    count = 0
    if not len(single_child_nodes):
        print(-1)
    else:
        for i in single_child_nodes:
            count = i.count + count
    return count
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
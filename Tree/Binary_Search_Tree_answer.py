"""
Binary Search Tree

Name: <your name>
"""

"""
Binary Search Tree (BST) is a binary tree that follows the following conditions:
    - The left subtree of a node contains only nodes with keys lesser than the node's key
    - The right subtree of a node contains only nodes with keys greater than the node's key
    - The left and right subtree each must also be a binary search tree
    
BST has the following advantages over arrays:
    - Dynamic size
    - Ease of insertion/deletion
    
BST has the following methods:
    - insert(data): Insert a node with the given data to the BST.
    - delete(data): Delete the first node with the given data from the BST.
    - search(data): Search for the first node with the given data in the BST.

Time Complexity:
    - insert(data): O(log n)
    - delete(data): O(log n)
    - search(data): O(log n)
    
Space Complexity: O(n)

BST limitations:
    - BST can be unbalanced, which means that the height of the tree can be O(n)
    - BST can be degenerate, which means that the height of the tree can be O(n)
    
BST vs Linked List:
    - BST is a binary tree, while Linked List is a linear data structure
    - BST is ordered, while Linked List is unordered
    - BST has a search time of O(log n), while Linked List has a search time of O(n) 
"""

# Binary Search Tree implementation

from collections import deque


class Node:
    """
    A Node class that will be used as the basic structure in our Binary Search Tree.

    Attributes:
    key (int): The key value of the node.
    left (Node): The left child node.
    right (Node): The right child node.
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    A class representing a Binary Search Tree.

    Attributes:
    root (Node): The root node of the tree.
    """

    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Inserts a new key in the BST. If the BST is empty, the new key becomes the root.
        If the BST is not empty, the new key is inserted in the correct position.
        If the key already exists in the BST, the key is not inserted.

        Parameters:
        key (int): The key to be inserted.
        """
        # TODO: Write your code here

        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(key, self.root)

    def _insert_recursive(self, key, node):
        """A helper method which implements the recursive process of insertion."""

        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(key, node.left)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(key, node.right)

    def delete(self, key):
        """
        Deletes a node with the specified key from the BST. If the node does not exist, the BST remains unchanged.

        Parameters:
        key (int): The key of the node to be deleted.
        """
        # TODO: Write your code here

        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        """A helper method which implements the recursive process of node deletion."""

        # If the tree is empty
        if node is None:
            return node

        # Traverse to the correct node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:  # node.key == key, delete the node
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children, get the inorder successor (smallest in the right subtree)
            node.key = self._min_value_node(node.right).key

            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, node.key)

        return node

    def _min_value_node(self, node):
        """Helper method to find the node with the minimum key in a subtree."""

        current = node

        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current

    def search(self, key):
        """
        Searches for a node with a given key in the BST.

        Parameters:
        key (int): The key to search for.

        Returns:
        Node: The node with the given key if it exists, None otherwise.
        """
        # TODO: Write your code here

        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """
        A helper method that implements the recursive search process.

        Parameters:
        node (Node): The current node.
        key (int): The key to search for.

        Returns:
        Node: The node with the given key if it exists, None otherwise.
        """

        # Base Cases: root is null or key is present at root
        if node is None or node.key == key:
            return node

        # Key is greater than root's key
        if node.key < key:
            return self._search_recursive(node.right, key)

        # Key is smaller than root's key
        return self._search_recursive(node.left, key)

    def inorder_traversal(self):
        """
        Performs an in-order traversal of the tree and returns a list of visited nodes.
        """
        # TODO: Write your code here
        inorder_list = []
        self._inorder_recursive(self.root, inorder_list)
        return inorder_list

    def _inorder_recursive(self, node, arr):
        if node is None:
            return
        self._inorder_recursive(node.left, arr)
        arr.append(node.key)
        self._inorder_recursive(node.right, arr)

    def preorder_traversal(self):
        """
        Performs a pre-order traversal of the tree and returns a list of visited nodes.
        """
        # TODO: Write your code here
        preorder_list = []
        self._preorder_recursive(self.root, preorder_list)
        return preorder_list

    def _preorder_recursive(self, node, arr):
        if node is None:
            return
        arr.append(node.key)
        self._preorder_recursive(node.left, arr)
        self._preorder_recursive(node.right, arr)

    def postorder_traversal(self):
        """
        Performs a post-order traversal of the tree and returns a list of visited nodes.
        """
        # TODO: Write your code here
        postorder_list = []
        self._postorder_recursive(self.root, postorder_list)
        return postorder_list

    def _postorder_recursive(self, node, arr):
        if node is None:
            return
        self._postorder_recursive(node.left, arr)
        self._postorder_recursive(node.right, arr)
        arr.append(node.key)

    def get_height(self):
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, node):
        if node is None:
            return -1
        return 1 + max(self._get_height_recursive(node.left), self._get_height_recursive(node.right))


def test_bst():
    print("Testing Binary Search Tree implementation...", end="")
    # Test Node creation
    node = Node(1)
    assert node.key == 1
    assert node.left is None
    assert node.right is None

    # Test BST initialization
    bst = BinarySearchTree()
    assert bst.root is None

    # Test BST insertion
    bst.insert(50)
    assert bst.root.key == 50
    bst.insert(30)
    assert bst.root.left.key == 30
    bst.insert(70)
    assert bst.root.right.key == 70
    bst.insert(20)
    assert bst.root.left.left.key == 20
    bst.insert(40)
    assert bst.root.left.right.key == 40
    bst.insert(80)
    assert bst.root.right.right.key == 80
    '''
    Here is visual representation of the tree:
            50
           /  \
          30    70
        /  \      \
      20    40     80
    '''

    # Test BST search
    assert bst.search(50) == bst.root
    assert bst.search(30) == bst.root.left
    assert bst.search(70) == bst.root.right
    assert bst.search(20) == bst.root.left.left
    assert bst.search(40) == bst.root.left.right
    assert bst.search(80) == bst.root.right.right
    assert bst.search(100) is None
    assert bst.search(10) is None

    # Test BST inorder traversal
    assert bst.preorder_traversal() == [50, 30, 20, 40, 70, 80]
    assert bst.inorder_traversal() == [20, 30, 40, 50, 70, 80]
    assert bst.postorder_traversal() == [20, 40, 30, 80, 70, 50]

    # Test BST deletion
    bst.delete(80)  # Remove leaf node
    assert bst.root.right.right is None

    bst.insert(80)  # Add leaf node back
    bst.delete(70)  # Remove node with one child
    assert bst.root.right.key == 80

    bst.delete(30)  # Remove node with two children
    assert bst.root.left.key == 40
    assert bst.root.left.left.key == 20

    '''
    Here is visual representation of the tree:
            50
           /  \
          40    80
         /  
       20
    '''
    assert (bst.preorder_traversal() == [50, 40, 20, 80])
    assert (bst.inorder_traversal() == [20, 40, 50, 80])
    assert (bst.postorder_traversal() == [20, 40, 80, 50])

    # Test BST height
    assert (bst.get_height() == 2)

    """
    Test Larger BST ------------------------------------------------------------------------
    """
    # Test BST initialization
    bst = BinarySearchTree()
    assert bst.root is None

    # Test BST insertion
    bst.insert(50)
    assert bst.root.key == 50
    bst.insert(30)
    assert bst.root.left.key == 30
    bst.insert(70)
    assert bst.root.right.key == 70
    bst.insert(20)
    assert bst.root.left.left.key == 20
    bst.insert(40)
    assert bst.root.left.right.key == 40
    bst.insert(80)
    assert bst.root.right.right.key == 80
    bst.insert(10)
    assert bst.root.left.left.left.key == 10
    bst.insert(25)
    assert bst.root.left.left.right.key == 25
    bst.insert(35)
    assert bst.root.left.right.left.key == 35

    # Test BST search
    assert bst.search(50) == bst.root
    assert bst.search(30) == bst.root.left
    assert bst.search(70) == bst.root.right
    assert bst.search(20) == bst.root.left.left
    assert bst.search(40) == bst.root.left.right
    assert bst.search(80) == bst.root.right.right
    assert bst.search(25) == bst.root.left.left.right
    assert bst.search(100) is None
    assert bst.search(5) is None
    assert bst.search(45) is None
    assert bst.search(60) is None

    # Test BST inorder traversal
    assert bst.preorder_traversal() == [50, 30, 20, 10, 25, 40, 35, 70, 80]
    assert bst.inorder_traversal() == [10, 20, 25, 30, 35, 40, 50, 70, 80]
    assert bst.postorder_traversal() == [10, 25, 20, 35, 40, 30, 80, 70, 50]

    # Test BST deletion
    bst.delete(80)  # Remove leaf node
    assert bst.root.right.right is None

    bst.insert(80)  # Add leaf node back
    bst.delete(70)  # Remove node with one child
    assert bst.root.right.key == 80

    bst.delete(30)  # Remove node with two children
    assert bst.root.left.key == 35
    assert bst.root.left.right.key == 40

    '''
    Here is visual representation of the tree:
            50
           /  \
         35    80
        /  \
       20  40
      /  \
    10    25
    '''

    assert (bst.preorder_traversal() == [50, 35, 20, 10, 25, 40, 80])
    assert (bst.inorder_traversal() == [10, 20, 25, 35, 40, 50, 80])
    assert (bst.postorder_traversal() == [10, 25, 20, 40, 35, 80, 50])

    bst.insert(70)
    bst.insert(75)
    assert (bst.inorder_traversal() == [10, 20, 25, 35, 40, 50, 70, 75, 80])
    '''
    Here is visual representation of the tree:
            50
           /  \
         35    80
        /  \   /
       20  40 70
      /  \      \
    10    25    75
    '''

    bst.delete(50)
    assert bst.root.key == 70
    assert bst.root.right.key == 80
    assert bst.root.right.left.key == 75

    '''
    Here is visual representation of the tree:
            70
           /  \
         35    80
        /  \   /
       20  40 75
      /  \
    10    25
    '''

    assert (bst.preorder_traversal() == [70, 35, 20, 10, 25, 40, 80, 75])
    assert (bst.inorder_traversal() == [10, 20, 25, 35, 40, 70, 75, 80])
    assert (bst.postorder_traversal() == [10, 25, 20, 40, 35, 75, 80, 70])

    # Test BST height
    assert (bst.get_height() == 3)
    print("Passed all tests!")


if __name__ == "__main__":
    test_bst()

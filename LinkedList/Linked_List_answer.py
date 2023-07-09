"""
Linked List

Name: <your name>
"""

"""
Linked List is a data structure that stores a collection of items.
Each item is connected to the next item through a link.

Linked List has two types of nodes:
    1. Head Node: The first node in the list
    2. Tail Node: The last node in the list
    
Each node contains two items:
    1. Data: The data that we want to store
    2. Next: The reference to the next node in the list
    
Linked List is a dynamic data structure, which means that it can grow and shrink at runtime by allocating and deallocating memory.
It means that we don't need to give the size of the linked list at the beginning.

Linked List is a linear data structure, which means that it can be traversed in one direction.

Linked List has the following advantages over arrays:
    1. Dynamic size
    2. Ease of insertion/deletion
    
Linked List has the following methods:
    1. append(data): Add a node with the given data to the end of the linked list.
    2. insert(data, position): Insert a node with the given data at the given position.
    3. delete(data): Delete the first node with the given data.
    4. display(): Display the linked list.
    
Time Complexity:
    1. append(data): O(n)
    2. insert(data, position): O(n)
    3. delete(data): O(n)
    4. display(): O(n)
    
Space Complexity: O(n)
"""


class Node:
    """Class representing a node in a singly linked list."""

    def __init__(self, data=None):
        """
        Initialize a node.

        Args:
            data: Data to be stored in the node. Defaults to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """Class representing a singly linked list."""

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def append(self, data):
        """
        Add a node with the given data to the end of the linked list.

        Args:
            data: Data to be stored in the new node.
        """
        # hints
        # 1. create a new node
        # 2. if the linked list is empty, set the head to the new node
        # 3. else, traverse the linked list until the last node
        # 4. set the next of the last node to the new node
        if not self.head:
            self.head = Node(data)
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = Node(data)

    def insert(self, data, position):
        """
        Insert a node with the given data at the given position.

        Args:
            data: Data to be stored in the new node.
            position: Index where the new node should be inserted.
                      If position is out of range, the node is appended at the end.
        """
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr_node = self.head
            pos = 0
            while pos < position - 1 and curr_node.next:
                curr_node = curr_node.next
                pos += 1
            new_node.next = curr_node.next
            curr_node.next = new_node

    def delete(self, data):
        """
        Delete the first node with the given data.

        Args:
            data: Data to be deleted from the linked list.
        """
        if self.head and self.head.data == data:
            self.head = self.head.next
            return

        curr_node = self.head
        while curr_node and curr_node.next:
            if curr_node.next.data == data:
                curr_node.next = curr_node.next.next
                break
            curr_node = curr_node.next

    def display(self):
        """
        Display the linked list.

        Returns:
            A list containing the data from each node.
        """
        nodes = []
        curr_node = self.head
        while curr_node:
            nodes.append(curr_node.data)
            curr_node = curr_node.next
        return nodes


"""
Test Cases for Linked List -----------------------------
"""


def test_linked_list():
    print("Testing Linked List...", end='')
    # Test Node creation
    node = Node(1)
    assert node.data == 1
    assert node.next == None

    # Test LinkedList initialization
    linked_list = LinkedList()
    assert linked_list.head == None

    # Test appending nodes to the LinkedList
    linked_list.append(1)
    assert linked_list.display() == [1]

    linked_list.append(2)
    assert linked_list.display() == [1, 2]

    linked_list.append(3)
    assert linked_list.display() == [1, 2, 3]

    # Test inserting nodes into the LinkedList
    linked_list.insert(0, 0)  # Inserting at the start
    assert linked_list.display() == [0, 1, 2, 3]

    linked_list.insert(1.5, 2)  # Inserting in the middle
    assert linked_list.display() == [0, 1, 1.5, 2, 3]

    linked_list.insert(4, 100)  # Inserting out of range
    assert linked_list.display() == [0, 1, 1.5, 2, 3, 4]

    # Test deleting nodes from the LinkedList
    linked_list.delete(0)  # Deleting the first element
    assert linked_list.display() == [1, 1.5, 2, 3, 4]

    linked_list.delete(2)  # Deleting an element in the middle
    assert linked_list.display() == [1, 1.5, 3, 4]

    linked_list.delete(4)  # Deleting the last element
    assert linked_list.display() == [1, 1.5, 3]

    linked_list.delete(10)  # Deleting a non-existent element
    assert linked_list.display() == [1, 1.5, 3]
    print("Passed!")


if __name__ == '__main__':
    test_linked_list()

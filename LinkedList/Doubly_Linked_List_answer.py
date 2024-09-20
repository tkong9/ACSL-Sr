'''
Doubly Linked List

Name: <Your Name>
'''

"""
Double linked list is a data structure that supports the following operations:
    - prepend: add a node with the given data to the beginning of the linked list
    - append: add a node with the given data to the end of the linked list
    - search: search for a node with the given data in the linked list
    - remove: remove the first node with the given data from the linked list
    - insert: insert a node with the given data at the given position
    
Time Complexity:
    - prepend: O(1)
    - append: O(1)
    - search: O(n)
    - remove: O(n)
    - insert: O(n)
    
Space Complexity:
    - O(n)

Doubly Linked List is a type of linked list in which each node apart from storing its data has two links.
The first link points to the previous node in the list and the second link points to the next node in the list.

The first node of the list has its previous link pointing to NULL similarly the last node of the list has its next
link pointing to NULL.

The following is an example of a doubly linked list with 5 nodes.
NULL <- 1 <-> 2 <-> 3 <-> 4 <-> 5 -> NULL

The following is an example of a doubly linked list with 3 nodes.
NULL <- 1 <-> 2 <-> 3 -> NULL
"""


class Node:
    """
    Node class represents a node in a doubly linked list.
    It has a value and two links: to the next node and to the previous one.
    """
    def __init__(self, data=None):
        """
        Initialize a node with given data.
        """
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    DoublyLinkedList class represents a doubly linked list.
    """
    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Append a new node with the given data to the end of the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """
        Prepend a new node with the given data to the start of the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert(self, data, position):
        """
        Insert a new node with the given data at the specified position in the list.
        Position is 0-based, i.e., position = 0 inserts at the head, and position beyond end of list appends to the list.
        """
        if position <= 0:
            self.prepend(data)
        else:
            new_node = Node(data)
            curr_node = self.head
            for _ in range(position - 1):
                if curr_node.next is not None:
                    curr_node = curr_node.next
                else:
                    break
            if curr_node.next is None:  # We're at the end of the list or the list is empty
                self.append(data)
            else:
                new_node.next = curr_node.next
                new_node.prev = curr_node
                curr_node.next.prev = new_node
                curr_node.next = new_node

    def search(self, data):
        """
        Search for the first node with the given data.
        If found, return the node. Otherwise, return None.
        """
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                return curr_node
            curr_node = curr_node.next
        return None

    def remove(self, data):
        """
        Remove the first node with the given data.
        If the node is not found, do nothing.
        """
        node_to_remove = self.search(data)
        if node_to_remove is None:
            return
        if node_to_remove.prev is not None:
            node_to_remove.prev.next = node_to_remove.next
        if node_to_remove.next is not None:
            node_to_remove.next.prev = node_to_remove.prev
        if node_to_remove is self.head:
            self.head = self.head.next
        if node_to_remove is self.tail:
            self.tail = self.tail.prev

    def print_list(self):
        """
        Print the data in the list from head to tail.
        """
        dll_list = []
        curr_node = self.head
        while curr_node:
            dll_list.append(curr_node.data)
            curr_node = curr_node.next

        return dll_list


def test_doubly_linked_list():
    print("Testing doubly linked list operations...", end="")
    dll = DoublyLinkedList()

    # Test operations on an empty list
    assert dll.print_list() == []

    # Test appending elements
    dll.append(1)
    assert dll.print_list() == [1]
    assert dll.head.data == 1
    assert dll.tail.data == 1

    dll.append(2)
    assert dll.print_list() == [1, 2]
    assert dll.head.data == 1
    assert dll.tail.data == 2

    # Test prepending elements
    dll.prepend(0)
    assert dll.print_list() == [0, 1, 2]
    assert dll.head.data == 0
    assert dll.tail.data == 2

    # Test inserting elements
    dll.insert(-1, 0)
    assert dll.print_list() == [-1, 0, 1, 2]
    assert dll.head.data == -1
    assert dll.tail.data == 2

    dll.insert(1.5, 3)
    assert dll.print_list() == [-1, 0, 1, 1.5, 2]
    assert dll.head.data == -1
    assert dll.tail.data == 2

    # Test inserting elements beyond the end of the list
    dll.insert(3, 100)
    assert dll.print_list() == [-1, 0, 1, 1.5, 2, 3]
    assert dll.head.data == -1
    assert dll.tail.data == 3

    # Test inserting elements at the end of the list
    dll.insert(4, 6)
    assert dll.print_list() == [-1, 0, 1, 1.5, 2, 3, 4]
    assert dll.head.data == -1
    assert dll.tail.data == 4

    # Test searching for elements
    assert dll.search(-1) is not None
    assert dll.search(4) is not None
    assert dll.search(100) is None

    # Test removing elements
    dll.remove(-1)
    assert dll.print_list() == [0, 1, 1.5, 2, 3, 4]
    assert dll.head.data == 0
    assert dll.tail.data == 4

    dll.remove(4)
    assert dll.print_list() == [0, 1, 1.5, 2, 3]
    assert dll.head.data == 0
    assert dll.tail.data == 3

    dll.remove(1.5)
    assert dll.print_list() == [0, 1, 2, 3]
    assert dll.head.data == 0
    assert dll.tail.data == 3

    dll.remove(0)
    assert dll.print_list() == [1, 2, 3]
    assert dll.head.data == 1
    assert dll.tail.data == 3

    # Test removing non-existing elements
    dll.remove(100)
    assert dll.print_list() == [1, 2, 3]
    assert dll.head.data == 1
    assert dll.tail.data == 3

    print("Passed!")


if __name__ == '__main__':
    test_doubly_linked_list()

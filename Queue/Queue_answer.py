"""
Queue

Name: <your name>
"""

"""
Queue is a data structure that is similar to a list, but with a few differences.
Queue follows the FIFO (First In First Out) principle.
Queue is used in many applications such as:
    - Breadth First Search (BFS)
    - Implementing cache
    - Implementing a printer queue
    - etc.
    
Queue operations:
    - enqueue(item) - adds an item to the end of the queue
    - dequeue() - removes the first item from the queue
    - peek() - returns the first item from the queue without removing it
    - is_empty() - returns True if the queue is empty, False otherwise
    - size() - returns the number of items in the queue
    
Queue implementation:
    - Using a list
    - Using a linked list
    
Queue applications:
    - Breadth First Search (BFS)
    - Implementing cache
    - Implementing a printer queue
    - etc.
    
Queue complexity:
    - enqueue(item) - O(1)
    - dequeue() - O(1)
    - peek() - O(1)
    - is_empty() - O(1)
    - size() - O(1)
    
Queue limitations:
    - Queue size is fixed (depends on the implementation)
    - Queue can overflow (depends on the implementation)
    - Queue can underflow (depends on the implementation)
    
Queue vs Stack:
    - Queue follows the FIFO (First In First Out) principle
    - Stack follows the LIFO (Last In First Out) principle
"""

# Queue can be implemented using a list, but it is not efficient because
# deleting at the beginning of a list is O(n) since all the
# elements have to be shifted by one. Instead, we can use a collections.deque
# which is a double-ended queue and supports efficient addition and removal
# of elements from both sides.

# Queue implementation using a deque


from collections import deque


class Queue:
    """
    A simple implementation of a Queue data structure.
    This Queue provides FIFO functionality using Python's built-in deque.
    """

    def __init__(self):
        """Initialize an empty Queue."""
        self.queue = deque()

    def enqueue(self, item):
        """
        Add an element to the end of the Queue.

        Parameters:
        item (any): The item to add to the Queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Remove an element from the front of the Queue.

        Returns:
        The item removed from the Queue. If the Queue is empty, returns None.
        """
        if len(self.queue) < 1:
            return None
        return self.queue.popleft()

    def peek(self):
        """
        Return the element at the front of the Queue without removing it.

        Returns:
        The item at the front of the Queue. If the Queue is empty, returns None.
        """
        if len(self.queue) < 1:
            return None
        return self.queue[0]

    def is_empty(self):
        """
        Check if the Queue is empty.

        Returns:
        True if the Queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def size(self):
        """
        Get the number of items in the Queue.

        Returns:
        The number of items in the Queue.
        """
        return len(self.queue)

    def display(self):
        """
        Display the content of the Queue.

        Returns:
        A list representation of the Queue.
        """
        return list(self.queue)


def is_palindrome(s):
    """
    Check if a string is a palindrome using a Queue.
    You can also you other data structures such as a Stack.
    Assume that the string only contains lowercase letters and no spaces.

    Parameters:
    s (str): The string to check.

    Returns:
    True if the string is a palindrome, False otherwise.
    """
    queue = Queue()
    stack = list(s)

    for char in s:
        queue.enqueue(char)

    while queue.is_empty() is False:
        if queue.dequeue() != stack.pop():
            return False

    return True


"""
Test cases for Queue implementation. ----------------------------
"""


def test_queue():
    print("Testing Queue implementation...", end="")
    queue = Queue()
    assert queue.is_empty() is True
    assert queue.size() == 0
    queue.enqueue("Apple")
    assert queue.display() == ["Apple"]
    queue.enqueue("Banana")
    assert queue.display() == ["Apple", "Banana"]
    assert queue.peek() == "Apple"
    assert queue.dequeue() == "Apple"
    assert queue.display() == ["Banana"]
    assert queue.is_empty() is False
    assert queue.size() == 1
    print("Passed!")


def test_is_palindrome():
    print("Testing is_palindrome()...", end="")
    assert is_palindrome("racecar") is True
    assert is_palindrome("apple") is False
    assert is_palindrome("a") is True
    assert is_palindrome("") is True
    assert is_palindrome("ab") is False
    assert is_palindrome("abc") is False
    assert is_palindrome("abcd") is False
    assert is_palindrome("abcde") is False
    assert is_palindrome('kayak') is True
    assert is_palindrome('rotor') is True
    assert is_palindrome('우영우') is True
    assert is_palindrome('역삼역') is True
    assert is_palindrome('기러기') is True
    assert is_palindrome('대한민국') is False
    print("Passed!")


def test_all():
    # Comment out the tests you do not wish to run!
    test_queue()
    test_is_palindrome()


if __name__ == '__main__':
    test_all()

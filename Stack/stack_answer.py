"""
Stack

Name: <your name>
"""

"""
Stack ADT (Abstract Data Type) is a data structure that follows the LIFO (Last In First Out) principle.
Stacks are used in many applications such as:
    - Function calls
    - Undo/Redo
    - Backtracking
    - Expression evaluation and syntax parsing
    - Memory management
    - etc.
    
Stack operations:
    - push(item) - adds an item to the top of the stack
    - pop() - removes the top item from the stack
    - peek() - returns the top item from the stack without removing it
    - is_empty() - returns True if the stack is empty, False otherwise
    - size() - returns the number of items in the stack
    
Stack implementation:
    - Using a list
    - Using a linked list
    
Stack applications:
    - Reversing a string
    - Balancing parentheses
    - Infix, prefix, postfix expressions
    - Implementing undo/redo
    - Implementing backtracking
    - Implementing call stack
    - Implementing memory stack
    - etc.
    
Stack complexity:
    - push(item) - O(1)
    - pop() - O(1)
    - peek() - O(1)
    - is_empty() - O(1)
    - size() - O(1)
    
Stack limitations:
    - Stack size is fixed (depends on the implementation)
    - Stack can overflow (depends on the implementation)
    - Stack can underflow (depends on the implementation)
"""


# Stack implementation using a list
class Stack:
    def __init__(self):
        self.stack = []

    # Method to add data to the stack
    # Adds to the end of the list
    def push(self, data):
        self.stack.append(data)

    # Method to remove data from the stack
    # Removes from the end of the list
    # Returns None if stack is empty
    # Returns the popped item otherwise
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    # Method to check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Method to view the top element of the stack
    # Returns None if stack is empty
    # Returns the top element otherwise
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    # Method to view all elements of the stack
    # Returns the stack
    def get_stack(self):
        return self.stack


# Use the Stack class you implemented above to solve the following problems


# Function to reverse a string using a stack
# s: string
# return: reversed string
def reverse_string(s):
    stack = Stack()

    for char in s:
        stack.push(char)

    reversed_str = ""
    while len(stack.stack):
        reversed_str += stack.pop()

    return reversed_str


# Function to check if parentheses are balanced
# You can assume that the string only contains braces and no other characters.
# The braces consist of (), [], and {}. You can also assume that empty string is balanced.
# s: string
# return: True if balanced, False otherwise
def is_balanced(s):
    # stack = Stack()
    # opening_brackets = ["(", "{", "["]
    # closing_brackets = [")", "}", "]"]
    #
    # for bracket in s:
    #     if bracket in opening_brackets:
    #         stack.push(bracket)
    #     elif bracket in closing_brackets:
    #         if stack.is_empty() or opening_brackets[closing_brackets.index(bracket)] != stack.pop():
    #             return False
    # return stack.is_empty()

    stack = Stack()
    for bracket in s:
        if bracket == '(' or bracket == '{' or bracket == '[':
            stack.push(bracket)
            continue
        if not stack.is_empty() and bracket == ')' and stack.peek() == '(':
            stack.pop()
        elif not stack.is_empty() and bracket == '}' and stack.peek() == '{':
            stack.pop()
        elif not stack.is_empty() and bracket == ']' and stack.peek() == '[':
            stack.pop()
        else:
            return False
    return stack.is_empty()


"""
Test Cases-----------------------------------------------------------------------
"""


# Testing the Stack class
def test_stack():
    print('Testing Stack class...', end='')
    # Instantiate the Stack class
    s = Stack()

    # Test if new stack is empty
    assert s.is_empty() == True

    # Test push method
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.get_stack() == [1, 2, 3]

    # Test peek method
    assert s.peek() == 3

    # Test pop method
    assert s.pop() == 3
    assert s.get_stack() == [1, 2]

    # Test is_empty method
    assert s.is_empty() == False

    # Test pop method
    assert s.pop() == 2

    # Test peek method
    assert s.peek() == 1

    # Test pop method
    assert s.pop() == 1
    assert s.pop() == None

    # Test peek method
    assert s.peek() == None
    print('Passed!')


def test_reverse_string():
    print('Testing reverse_string()...', end='')
    assert reverse_string('') == ''
    assert reverse_string('a') == 'a'
    assert reverse_string('ab') == 'ba'
    assert reverse_string('abc') == 'cba'
    assert reverse_string('abcd') == 'dcba'
    assert reverse_string('abcde') == 'edcba'
    assert reverse_string('Hello, World!') == '!dlroW ,olleH'
    print('Passed!')


def test_is_balanced():
    print('Testing is_balanced()...', end='')
    assert is_balanced('') == True
    assert is_balanced('[]') == True
    assert is_balanced('()') == True
    assert is_balanced('{}') == True
    assert is_balanced('[](){}') == True
    assert is_balanced('[()]{}') == True
    assert is_balanced('[([]{})]') == True
    assert is_balanced('[([]{})]((())){}') == True
    assert is_balanced('[([]{})]()[{}]') == True
    assert is_balanced('[([]{})][(){}]') == True
    assert is_balanced('[') == False
    assert is_balanced(']') == False
    assert is_balanced('][') == False
    assert is_balanced('[][') == False
    assert is_balanced('[(]}') == False
    assert is_balanced('[(]{})') == False
    assert is_balanced('[([]{})](){}]') == False
    assert is_balanced('()[][([]{})](){}(') == False
    assert is_balanced('{{{{{{{{{') == False
    assert is_balanced('}}}}}}}}') == False
    assert is_balanced('(}') == False
    assert is_balanced('[(])') == False
    print('Passed!')


def test_all():
    test_stack()
    test_reverse_string()
    test_is_balanced()


if __name__ == '__main__':
    test_all()

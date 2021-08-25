"""
This module holds the stack class.
 And the input class
"""

class Stack:
    """
    A stack that supports operations
    """
    def __init__(self):
        self.s = []

    def pop(self):
        return self.s.pop()

"""
This module holds the implementation
 for the AstNodes and Tokens
 Also this module holds some related functions as well
"""
from enum import Enum, auto

class TType(Enum):
    NUMBER = auto()
    LITERAL = auto()

class Token:
    def __init__(self, value, _t):
        self.value = value
        self.type = _t
        self.things = {}

    def update(self, things):
        self.things = things

    def __repr__(self):
        return f"Token({repr(self.value)}, {self.type}, {self.things})"

class ASTType(Enum):
    NUMBER = auto()
    KEYWORD = auto()

class ASTNode:
    """
    An ASTNode

    value: Token

    type: ASTType

    children: list(ASTNode)
    """
    def __init__(self, value, _type):
        self.value = value
        self.type = _type
        self.children = []

def get_closing_token(tokens, open, close):
    """
    Get the index of the closing token corresponding
     to the opening token. For example. `( () )` will return
     the last element's index

    tokens: list(Token)
     Tokens to parse through.

    open: str
     Opening string

    close: str
     Corresponding closing string
    """
    is_bound = 0   # Lookout for nested open/close pairs
    found_start = False
    index = -1    # -1 means the last element (for fallback)

    i = 0
    while i < len(tokens):
        token = tokens[i]
        char = token.value

        if char == open:
            if not found_start: found_start = True
            is_bound += 1

        elif char == close:
            is_bound -= 1
            if is_bound == 0:
                index = i
                break
        i += 1

    return index

def get_nested_level(tokens, open, close):
    """
    Get the level of nested. 0 if not nested

    tokens: list(Token)
     Tokens to parse through.

    open: str
     Opening string

    close: str
     Corresponding closing string
    """
    k = 0
    for token in tokens:
        if token.value == open:
            k += 1
        if token.value == close:
            k -= 1
    return k + 1

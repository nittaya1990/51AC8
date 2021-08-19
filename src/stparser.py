"""
The parser module for 51AC8
"""
from enum import Enum, auto
import re

COMMANDS = '+-×÷'

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

def split(string):
    """
    Removes comments and splits code.

    string: str
     The code to split

    returns: list(str)
     splitted code
    """
    string = re.sub(r'#.*', '', string)
    string = (
            string.replace('(', ' ( ')
            .replace(')', ' ) ')
            .replace('[', ' [ ')
            .replace(']', ' ] ')
            .replace('{', ' { ')
            .replace('}', ' } ')
            )
    for char in COMMANDS:
        string = re.sub(r'[^K|\\]' + '\\' + char, ' ' + char + ' ', string)
    string = re.sub(r'(K.)',  r' \1 ', string)
    
    splitted = []
    temp = ''

    i = 0
    while i < len(string):
        char = string[i]
        i += 1

        if char == ' ' or char == '\n':
            if temp != '':
                splitted.append(temp)
            temp = ''
            continue

        temp += char

    if temp != '': splitted.append(temp)

    return splitted

def tokenise(splitted):
    """
    converts the list of strings
     to tokens

    splitted: list(str)
    
    returns: list(Token)
    """
    tokens = []

    i = -1
    for v in splitted:
        try: token = Token(int(v), TType.NUMBER)
        except:
            try: token = Token(float(v), TType.NUMBER)
            except:
                token = Token(v, TType.LITERAL)
        tokens.append(token)
        i += 1

    return tokens

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

def parse(tokens):
    """
    Add information to tokens. For example
     if the token is a bracket, find its matching bracket and
     store its index.
    
    tokens: list(Token)

    returns: list(Token)
    """
    i = 0
    while i < len(tokens):
        token = tokens[i]
        i += 1

if __name__ == "__main__":
    print(tokenise(split('2 3.45 3e100 1 1+-')))

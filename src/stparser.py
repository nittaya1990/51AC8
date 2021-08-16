"""
The parser module for 51AC8
"""
from enum import Enum, auto
import re

COMMANDS = '+-×÷'

class TType(Enum):
    NUMBER = auto()
    COMMAND = auto()
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
                token = Token(v, TType.COMMAND)
        if splitted[i] == '\\':
            token = Token(v, TType.LITERAL)
        tokens.append(token)
        i += 1

    return tokens

if __name__ == "__main__":
    print(tokenise(split('2 3.45 0.01 3e100 1 1+-')))

"""
The parser module for 51AC8
"""
from enum import Enum, auto
from stast import *
import re

COMMANDS = '+-×÷'

def split(string):
    """
    Removes comments and splits code.

    string: str
     The code to split

    returns: list(str)
     splitted code
    """
    string = re.sub(r'⍝.*', '', string)
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

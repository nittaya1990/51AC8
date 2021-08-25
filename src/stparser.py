"""
The parser module for 51AC8
"""
from stast import *
import re

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
    string = re.sub(r'(K.)',  r' \1 ', string)

    n_string = ''

    i = 0
    while i < len(string):
        char = string[i]
        try:
            next = string[i + 1]
        except:
            next = ''
        i += 1

        if char in 'λ@\\':
            n_string += char + next + ' '
            i += 1
            continue
        if char in '0123456789.e':
            n_string += string[i:dend(string, i)]

        n_string += char + ' '

    string = n_string

    
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
    print(tokenise(split('λf')))

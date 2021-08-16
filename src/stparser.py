"""
The parser module for 51AC8
"""
import re

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
    for char in "+=÷×":
        string = re.sub(r'(K|\\){0}' + '\\' + char, ' ' + char + ' ', string)
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

    return splitted

if __name__ == "__main__":
    print(split('2 1 1+-'))

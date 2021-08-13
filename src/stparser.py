"""
The parser module for 51AC8
"""
import re

def tokenise(string):
    """
    Removes comments and tokenises code.

    string: str
     The code to tokenise

    returns: list(str)
     tokenised code
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
    string = re.sub(r'(K.)',  r' \1 ', string)

"""
Matrix utilily functions.
As an extension to the python list
This module is standalone and does not depend on anything else.
"""

def depth(l):
    """
    Return the depth of l
    3 -> 0
    [] -> 1
    [[4, []], 3] -> 3
    
    l: list(any)
    """
    if not isinstance(l, list):
        return 0

    if not len(l):
        return 1

    d = max(list(map(depth, l))) + 1
    return d

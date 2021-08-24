"""
Matrix utilily functions.
As an extension to the python list
This module is standalone and does not depend on anything except the
ones found in the python standard library.
"""
from collections import deque
from itertools import zip_longest

def depth(l):
    """
    Return the depth of l
    3 -> 0
    [] -> 1
    [[4, []], 3] -> 3
    
    l: list(any) | any
    """
    if not isinstance(l, list):
        return 0

    if not len(l):
        return 1

    d = max(list(map(depth, l))) + 1
    return d

def reduce_first(f, l):
    """
    Reduce, on the first axis, function f over l
    
    f: dyadic function
    
    l: list(any) | any
    """
    if not isinstance(l, list):
        return l
    res = l[0]
    for x in l[1:]:
        res = f(res, x)
    return res

def vectorise2(f, x, y):
    """
    Jelly's generic vectorisation function.
    Ported from Jelly to Python
    
    Credit: caird coinheringaahing's jelly 
     answer https://codegolf.stackexchange.com/a/220832/103854
    
    f: dyadic function
    
    x: list(any) | any
    
    y: list(any) | any
    """
    dx = depth(x)
    dy = depth(y)
    if dx == dy:
        if dx != 0:
            return [vectorise2(f, a, b) for a,b in zip_longest(x, y, fillvalue=0)]
        else:
            return f(x, y)
    else:
        if dx < dy:
            return [vectorise2(f, x, b) for b in y]
        else:
            return [vectorise2(f, a, y) for a in x]

def reduce(f, l):
    """
    Reduce function f over l
    
    f: dyadic function
    
    l: list(any) | any
    """
    if not isinstance(l, list):
        return l
    if isinstance(l[0], list):
        return [reduce(f, x) for x in l]
    res = l[0]
    for x in l[1:]:
        res = f(res, x)
    return res

def _next(dq):
    """
    Rotates the dq left
    
    Credit: hyper-neutrino
    
    dq: deque
    """
    x = dq.popleft()
    dq.append(x)
    return x

def reshape(shape, l):
    """
    APL's reshape
    
    Credit: hyper-neutrino
    
    shape: list(int)
     the shape we want to reshape to
    
    l: list(any) | any
    """
    if not (isinstance(l, list) or isinstance(l, deque)):
        return l
    if not isinstance(l, deque):
        l = deque(l)
    if len(shape) == 1:
         return [_next(l) for x in range(shape[0])]
    else:
        return [reshape(shape[1:], l) for x in range(shape[0])]

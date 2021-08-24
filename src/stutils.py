"""
Matrix utilily functions.
As an extension to the python list
This module is standalone and does not depend on anything else.
"""
from collections import deque

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

def reduce(f, l):
    """
    Reduce function f over l
    
    f: dyadic function
    
    l: list(any)
    """
    if not isinstance(l, list):
        return l
    res = l[0]
    for x in l[1:]:
        res = f(res, x)
    return res

def next(dq):
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
    
    l: list
    """
	if not isinstance(l, deque): l = deque(l)
	if len(shape) == 1:
		return [next(l) for x in range(shape[0])]
	else:
		return [reshape(shape[1:], l) for x in range(shape[0])]

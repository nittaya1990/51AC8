import stutils

def test_depth_scalar():
    assert stutils.depth(0) == 0
    assert stutils.depth(4) == 0
    assert stutils.depth(21) == 0

def test_depth_nested():
    assert stutils.depth([]) == 1
    assert stutils.depth([2]) == 1
    assert stutils.depth([2, []]) == 2
    assert stutils.depth([[]]) == 2
    assert stutils.depth([[], [3, [5]]]) == 3

def test_split():
    assert stutils.split([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]

def test_rotate_first():
    assert stutils.rotate_first([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert stutils.rotate_first([[1, 5], [2, 6], [3, 7], [4, 8]]) == [[4, 8], [1, 5], [2, 6], [3, 7]]

def test_rotate():
    assert stutils.rotate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert stutils.rotate([[1, 5], [2, 6], [3, 7], [4, 8]]) == [[5, 1], [6, 2], [7, 3], [8, 4]]

def test_reverse_first():
    assert stutils.reverse_first([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert stutils.reverse_first([[1, 5], [2, 6], [3, 7], [4, 8]]) == [[4, 8], [3, 7], [2, 6], [1, 5]]

def test_reverse():
    assert stutils.reverse([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert stutils.reverse([[1, 5], [2, 6], [3, 7], [4, 8]]) == [[5, 1], [6, 2], [7, 3], [8, 4]]

def test_reduce_first():
    assert stutils.reduce_first(lambda x,y: x+y, [1, 2, 3, 4]) == 10
    assert stutils.reduce_first(lambda x,y: x+y, [[1, 5], [2, 6], [3, 7], [4, 8]]) == [1, 5, 2, 6, 3, 7, 4, 8]

def test_reduce():
    assert stutils.reduce(lambda x,y: x+y, [1, 2, 3, 4]) == 10
    assert stutils.reduce(lambda x,y: x+y, [[1, 5], [2, 6], [3, 7], [4, 8]]) == [6, 8, 10, 12]

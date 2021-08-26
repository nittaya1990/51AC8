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

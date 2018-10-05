""" Unit tests for array_stack.ArrayStack """

from dloud_ads import array_stack

def test_dummy():
    """ Test Definition"""
    the_queue = array_stack.ArrayStack()

    assert the_queue.is_empty()
    assert not the_queue

    the_queue.push(2)
    assert not the_queue.is_empty()
    assert len(the_queue) == 1
    assert the_queue.pop() == 2

    _ = [the_queue.push(x) for x in range(4)]
    assert len(the_queue) == 4
    assert [the_queue.pop() for x in range(4)] == [3, 2, 1, 0]
    assert not the_queue

    _ = [the_queue.push(x) for x in range(9)]
    assert len(the_queue) == 9

    _ = [the_queue.push(x) for x in range(2)]
    assert len(the_queue) == 11

    expected = [1, 0, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert [the_queue.pop() for x in range(11)] == expected

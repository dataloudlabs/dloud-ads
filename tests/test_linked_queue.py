""" Unit tests for linked_queue.LinkedQueue """

from dloud_ads import linked_queue

def test_dummy():
    """ Test definition"""

    the_queue = linked_queue.LinkedQueue()

    assert the_queue.is_empty()
    assert not the_queue

    the_queue.enqueue(2)
    assert not the_queue.is_empty()
    assert len(the_queue) == 1
    assert the_queue.dequeue() == 2

    _ = [the_queue.enqueue(x) for x in range(4)]
    assert len(the_queue) == 4
    assert [the_queue.dequeue() for x in range(4)] == [0, 1, 2, 3]
    assert not the_queue

    _ = [the_queue.enqueue(x) for x in range(9)]
    assert len(the_queue) == 9

    _ = [the_queue.enqueue(x) for x in range(2)]
    assert len(the_queue) == 11

    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 1]
    assert [the_queue.dequeue() for x in range(11)] == expected

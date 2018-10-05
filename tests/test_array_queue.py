""" Unit tests for array_queue.ArrayQueue """

from dloud_ads import array_queue

def test_dummy():
    """Test definition"""

    the_queue = array_queue.ArrayQueue()

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
    assert len(the_queue._data) == 10

    _ = [the_queue.enqueue(x) for x in range(2)]
    assert len(the_queue) == 11
    assert len(the_queue._data) == 20

    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 1]
    assert [the_queue.dequeue() for x in range(11)] == expected

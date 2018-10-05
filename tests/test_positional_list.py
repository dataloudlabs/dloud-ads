""" Unit tests for positional_list.PositionalList """

from dloud_ads import positional_list

def test_dummy():
    """Test definition"""

    the_list = positional_list.PositionalList()
    pos8 = the_list.add_last(8)
    assert pos8.element() == 8
    assert the_list.first().element() == pos8.element()
    pos5 = the_list.add_after(pos8, 5)
    assert pos5.element() == 5
    assert the_list.first().element() == 8
    assert the_list.last().element() == 5
    assert the_list.before(pos5).element() == 8
    assert the_list.after(pos8).element() == 5
    assert the_list.after(pos5) is None
    assert the_list.before(pos8) is None
    pos3 = the_list.add_before(pos5, 3)
    assert pos3.element() == 3
    assert [x for x in the_list] == [8, 3, 5]

    value5 = the_list.delete(the_list.last())
    assert value5 == 5
    assert len(the_list) == 2
    assert [x for x in the_list] == [8, 3]

    value8 = the_list.replace(pos8, 7)
    assert value8 == 8
    assert [x for x in the_list] == [7, 3]

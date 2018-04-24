from __future__ import with_statement

from pytest import raises

from docma import Docma


def test_simple():
    class TestSimple(Docma):
        """
        field1: str
        field2: int
        field3: boolean
        """
        pass

    t1 = TestSimple()
    t1.field1 = "foo"
    assert t1.field1 == "foo"

    with raises(AttributeError):
        t1.field2 = "12"

    t1.field2 = 12
    assert t1.field2 == 12

    t1.field3 = True
    assert t1.field3

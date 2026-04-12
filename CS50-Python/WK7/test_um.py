from um import count
import pytest


def test_um_count():
    assert count("um") == 1
    assert count("u.. um..") == 1
    assert count("yummy!") == 0
    assert count("um, hello?") == 1
    assert count("yum yum") == 0
    assert count("um, um, um...") == 3

def test_upper():
    assert count("UM???") == 1
    assert count("Um...") == 1

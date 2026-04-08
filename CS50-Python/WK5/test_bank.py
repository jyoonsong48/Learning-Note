from bank import value

def test_return_zero():
    assert value("hello") == 0
    assert value("HELLo") == 0

def test_return_twenty():
    assert value("hi") == 20
    assert value("HEYY") == 20

def test_return_hundred():
    assert value("get out!") == 100
    assert value("GET out!") == 100


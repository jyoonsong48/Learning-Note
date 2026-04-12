from numb3rs import validate
import pytest

def test_number_of_input():
    assert validate("1.1") == False
    assert validate("1") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4") == True

def test_is_period():
    assert validate("43,23,20.1") == False
    assert validate("1!2!.3%$") == False

def test_is_value_in_range():
    assert validate("2.3.45.76") == True
    assert validate("-1.3.20.2") == False
    assert validate("0.12.3050.12") == False

def test_is_value_number():
    assert validate("cat") == False
    assert validate("yipeeee :3") == False


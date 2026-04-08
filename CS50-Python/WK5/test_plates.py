from plates import is_valid

def test_plates():
    assert is_valid("CS50") == True

def test_numbers():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False

def test_text():
    assert is_valid("PI3.14") == False
    assert is_valid("!BA") == False

def test_length():
    assert is_valid("H") == False
    assert is_valid("OUTOFTIME") == False

def test_first_alpha():
    assert is_valid("21FOR") == False
    assert is_valid("1AB") == False
    assert is_valid("50") == False
    assert is_valid(" 7D") == False
    assert is_valid("7") == False

from plates import is_valid


def test_two_letters():
    assert is_valid("CS") == True
    assert is_valid("H") == False
    assert is_valid("59") == False


def test_number_of_characters():
    assert is_valid("GOCS50") == True
    assert is_valid("THISISCS50") == False
    assert is_valid("SUPER") == True


def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("GO50CS") == False
    assert is_valid("CS05") == False


def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS50 ") == False
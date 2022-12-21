from bank import value


def test_uppercase():
    assert value("HELLO, MICHAEL") == 0
    assert value("HI HI HOW'S IT GOING?") == 20
    assert value("WHAT'S UP?") == 100


def test_lowercase():
    assert value("hello, thomas") == 0
    assert value("hi how are you doing?") == 20
    assert value("welcome, how are you?") == 100


def test_mix():
    assert value("heLLo") == 0
    assert value("Hi, what's up?") == 20
    assert value("WhAT's up?") == 100
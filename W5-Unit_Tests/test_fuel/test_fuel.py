from fuel import convert, gauge
import pytest


def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("-1/0")

def test_integer():
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("2/3") == 67
    assert convert("0/7") == 0


def test_noninteger():
    with pytest.raises(ValueError):
        convert("cat/2")
        convert("1 2")
        convert("12")


def test_Xgreater():
    with pytest.raises(ValueError):
        convert("2/1")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(37) == "37%"
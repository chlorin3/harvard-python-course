from twttr import shorten


def test_uppercase():
    assert shorten("PYTHON JUNIOR") == "PYTHN JNR"
    assert shorten("MONOSPACE") == "MNSPC"


def test_lowercase():
    assert shorten("python junior") == "pythn jnr"
    assert shorten("monospace") == "mnspc"


def test_numbers():
    assert shorten("1992") == "1992"
    assert shorten("16.12.2022 10:45") == "16.12.2022 10:45"


def test_mix():
    assert shorten("pyThoN JuniOR MonOSPAcE 1992") == "pyThN JnR MnSPc 1992"
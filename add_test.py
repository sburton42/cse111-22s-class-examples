from add import add_numbers
import pytest

def test_add_numbers():
    assert add_numbers(12, 27) == 39

def test_add_numbers_negative():
    assert add_numbers(-12, 27) == 15
    assert add_numbers(-12, -27) == -39

def test_add_numbers_zero():
    assert add_numbers(0, 0) == 0


pytest.main(["-v", "--tb=line", "-rN", __file__])

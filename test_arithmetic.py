# content of test_sample.py
import pytest


def func(x):
    return x + 1

@pytest.mark.main
def test_answer():
    assert func(3) == 5




@pytest.mark.arithmetic
def test_add():
    assert True

@pytest.mark.arithmetic
def test_subtract():
    assert 10 - 5 == 5

@pytest.mark.arithmetic
def test_divide():
    assert 5 / 4 == 1
@pytest.mark.arithmetic
def test_multiply():
    assert 5 * 5 == 25

@pytest.mark.print
def test_print_something():
    print("hello")

@pytest.mark.print
def test_print_in_middle():
    print("hello middle")

@pytest.mark.print
def test_print_something_else():
    print("hello there")
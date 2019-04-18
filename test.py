import pytest
from test2 import *


def test_input():
    with pytest.raises(Exception):
        #assert awesome(-3) == 'fizz'
        awesome(-3)

def test_multiple3():
    assert awesome(3) == 'fizz'

def test_multiple5():
    assert awesome(5) == 'buzz'

def test_multipleboth():
    assert awesome(15)== 'fizzbuzz'

def test_return_int():
    assert awesome(2) == 2




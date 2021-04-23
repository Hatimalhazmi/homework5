import pytest
from mypkg.my_answers import iterator


#class Test(unittest.TestCase):
def test_iterator():
    assert iterator(10) == {0 1 2 3 4 5 6 7 8 9 10}

import pytest
from mypkg.my_answers import iterator


#class Test(unittest.TestCase):
def test_iterator():
    assert iterator(10) == (012345678910)

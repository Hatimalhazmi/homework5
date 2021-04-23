import pytest
from mypkg.my_answers import iterator


#class Test(unittest.TestCase):
def test_iterator():
 
	result = iterator(4)
	expected = "1 2 3 4"
	assert result == expected

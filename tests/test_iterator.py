import pytest
from mypkg.my_answers import iterator


#class Test(unittest.TestCase):
def test_iterator():
 
result = iterator(10)
	expected = 1:9
	assert result == expected

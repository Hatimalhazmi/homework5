import pytest
from mypkg.my_answers import iterator


#class Test(unittest.TestCase):
def test_iterator():
 	for i in iterator(9):
	#result = iterator(4)
		expected = 1
		assert result == expected

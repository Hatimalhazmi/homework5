import pytest
from mypkg.my_answers import iterator


#class Test(unittest.TestCase):
def test_iterator():
 	for i in iterator(9):
	#result = iterator(4)
		expected = 1 2 3 4 5 6 7 8 9
		assert result == expected

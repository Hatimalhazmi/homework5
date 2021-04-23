import pytest
from mypkg.my_answers import iterator


#class Test(unittest.TestCase):
def test_iterator():
 	#for i in iterator(1):
	assert  iterator(1) == 1

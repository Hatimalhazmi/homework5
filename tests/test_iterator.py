import pytest
from mypkg.my_answers import iterator
def test_always_passes():
    assert True


#class Test(unittest.TestCase):
def test_iterator():
 	for i in iterator():
    		assert i == 1

		#ans = Solution()
        	#self.assertEqual(ans.i == 1 )
	
#if __name__ == "__main__":

   # pytest.main()

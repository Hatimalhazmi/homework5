import pytest
from mypkg.my_answers import iterator


def test_iterator():
 	for i in iterator(5):
    		#assert i == 1
		assert(1 <= i <= 5)
			 
		#ans = Solution()
        	#self.assertEqual(ans.i == 1 )
	
#if __name__ == "__main__":

   # pytest.main()

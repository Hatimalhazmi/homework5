import pytest
from mypkg.my_answers import iterator


def test_iterator():
 	for i in iterator(5):
		
		assert i[1] == 1
	    	assert i[2] == 2
   		assert i[3] == 3
    		assert i[4] == 4
			 
		#ans = Solution()
        	#self.assertEqual(ans.i == 1 )
	
#if __name__ == "__main__":

   # pytest.main()

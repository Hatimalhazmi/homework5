  
import pytest
from mypkg.my_answers import iterator



def test_iterator():
  for i in iterator(2):
    		assert (i) == 1, 2

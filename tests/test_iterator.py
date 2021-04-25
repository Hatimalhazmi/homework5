  
import pytest
from mypkg.my_answers import iterator



def test_iterator():
  for i in iterator(1):
    		assert (i) == 1

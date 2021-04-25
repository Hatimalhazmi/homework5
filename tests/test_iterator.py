  
import pytest
from mypkg.my_answers import iterator



def test_iterator():
  i = [i for i in iterator(5)]
  assert (i) == [5, 6, 7, 8, 9, 10]

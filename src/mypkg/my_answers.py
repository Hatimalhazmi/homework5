  
#!/usr/bin/python

"""
Object Oriented Programming and Python Classes
"""

"""
QUESTION 1: 
========================================================================================================
Write a class with name iterator which creates iterator type that iterates from 1 to a given limit. 
For example, if the limit is 10, then it prints  1 2 3 4 5 6 7 8 9 10. 

sample output = [0, 1, 2 ,3 ,4 ,5 , 6, 7, 8, 9, 10] 

Hint: You could have three methods: __init__, __iter__, and _next_.
"""
# An iterable user defined type
class iterator:
 
    # Constructor
    def __init__(self, limit):
        self.limit = limit
 
    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 1
        return self
 
    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
 
        # Store current value ofx
        x = self.x
 
        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration
 
        # Else increment and return old value
        self.x = x + 1;
        return x
 
# Prints numbers from 0 to 10
#for i in iterator(1):
 #   print(i,end =" ")
    
"""
QUESTION 2: 
========================================================================================================
Write a class with name unique_subsets to get all possible unique subsets from a set of distinct integers.
Example:
Input : [1, 2, 3]
output: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

===========================
"""
class unique_subsets:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

#print(unique_subsets().sub_sets([1,2,3]))



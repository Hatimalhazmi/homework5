  
#!/usr/bin/python

"""
Python Functions and Recursions

"""
"""
QUESTION 1: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.
def generateParenthesis(N):
    results = []
"""
import itertools

def generateParenthesis(N):
    results = []

    def backtrack(parenthesis, opening, closing):
        if len(parenthesis) == 2 * N:
            results.append(parenthesis)
            return

        if opening < N:
            backtrack(parenthesis + '(', opening + 1, closing) # generate opening bracket

        if closing < opening:
            backtrack(parenthesis + ')', opening, closing + 1) # generate closing bracket

    backtrack('', 0, 0)
    return results
"""







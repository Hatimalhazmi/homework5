  
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

QUESTION 2: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:
=========================================
Input: "race a car"
Output: false
Write a function named isPalindrome that takes a string as an input and returns a bool as an output.

class Solution {
    public static boolean isPalindrome(String s) {
        if (s == null) return false;
        if (s.length() == 0) return true;
        s = s.toLowerCase().trim();
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            while (i < j && !Character.isLetterOrDigit(s.charAt(i))) i++ ;
            while (i < j && !Character.isLetterOrDigit(s.charAt(j))) j--;
            if (s.charAt(i++) != s.charAt(j--)) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        isPalindrome("A man, a plan, a canal: Panama");
    }








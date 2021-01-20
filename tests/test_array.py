import pytest

from mypkg.my_answers import generateParenthesis


def generateParenthesisCase(N):
    assert generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]


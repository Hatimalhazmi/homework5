
from mypkg.my_answers import generateParenthesis


def test_example1():
    assert generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]


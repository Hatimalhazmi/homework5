import pytest

from mypkg.my_answers import generateParenthesis


def generateParenthesisCase(N):
        func = Solution().generateParenthesis
        self.assertEqual(func(0), [""])
        self.assertEqual(func(-1), [])
        self.assertEqual(func(2), ["(())","()()"])
        self.assertEqual(func(3), ["((()))","(()())","(())()","()(())","()()()"])

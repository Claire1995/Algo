from collections import deque

answers = []
n = 0

def recursive(cntLeft, cntRight, s, n):
    print(s)
    if cntLeft<cntRight or cntLeft>n or cntRight>n:
        return
    elif cntLeft == n and cntRight == n:
        answers.append(s)
    else:
        recursive(cntLeft+1, cntRight, s+"(", n)
        recursive(cntLeft, cntRight+1, s+")", n)


class Solution(object):
    def generateParenthesis(self, n):
        cntLeft = 1
        cntRight = 0
        s = "("
        recursive(cntLeft, cntRight, s, n)
        return answers

print(Solution.generateParenthesis(0, 1))
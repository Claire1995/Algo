from collections import deque

class Solution(object):
    
    def __init__(self):
        self.answers = []     # This is init for each test case.
    
    def recursive(self, cntLeft, cntRight, s, n):
        if cntLeft<cntRight or cntLeft>n or cntRight>n:
            return
        elif cntLeft == n and cntRight == n:
            self.answers.append(s)
        else:
            Solution.recursive(self, cntLeft+1, cntRight, s+"(", n)
            Solution.recursive(self, cntLeft, cntRight+1, s+")", n)
    
    def generateParenthesis(self, n):
        cntLeft = 1
        cntRight = 0
        s = "("
        Solution.recursive(self, cntLeft, cntRight, s, n)
        return self.answers
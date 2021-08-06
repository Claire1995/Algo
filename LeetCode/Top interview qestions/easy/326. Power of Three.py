class Solution(object):
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        a = 3
        while a<=n:
            print(a)
            if a == n:
                return True
            a = a*3
        return False
            
        
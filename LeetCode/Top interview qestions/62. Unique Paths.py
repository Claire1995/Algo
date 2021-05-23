class Solution(object):
    def uniquePaths(self, m, n):
        cnt = 0
        m = m-1
        n = n-1
        if m == 0 or n == 0:
            print(1)
            return 1

        mf = Solution.factorial(self, m, 1)
        nf = Solution.factorial(self, n, 1)
        mnf = Solution.factorial(self, m+n, 1)

        print(int(mnf / (mf*nf)))
        return int(mnf / (mf*nf))

    def factorial(self, num, result):
        if num == 1:
            return result
        else:
            return Solution.factorial(self, num-1, result*num)
        
Solution.uniquePaths(0, 1, 10)
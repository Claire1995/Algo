class Solution(object):
        
    def recursive(self, n, hist):
        if n==1 or n==0:
            return 1
        
        if hist[n-1]!=-1:
            a = hist[n-1]
            print('a!')
        else:
            a = Solution.recursive(self, n-1, hist)
            hist[n-1] = a
            
        if hist[n-2]!=-1:
            b = hist[n-2]
            print('b!')
        else:
            b = Solution.recursive(self, n-2, hist)
            hist[n-2] = b
        
        return  a+b 
    
    def climbStairs(self, n):
        return Solution.recursive(self, n, [-1]*45)
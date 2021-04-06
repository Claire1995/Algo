class Solution(object):
    def minOperations(self, n):
        if n%2!=0:
            cnt = 0
            for i in range(2, n, 2):
                cnt = cnt+i
            return cnt
        else:
            cnt = 0
            for i in range(1, n+1, 2):
                print(i)
                cnt = cnt+i
            return cnt
        
print(Solution.minOperations(1, 31))
from collections import deque

class Solution(object):
    def findDuplicate(self, nums):
        n = max(nums)
        nums = deque(sorted(nums))
        prev = nums.pop()
        while nums:
            cur = nums.pop()
            if cur == prev:
                return cur
            prev = cur
               
        return cur
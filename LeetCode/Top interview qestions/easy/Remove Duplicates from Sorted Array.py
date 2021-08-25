class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        temp = 1000
        for i, n in enumerate(nums):
            if n!=temp:
                k += 1
                temp = n
            else:
                nums[i] = 1000
        nums.sort()
        print(nums)
        return k
        
class Solution(object):
    def findKthLargest(self, nums, k):
        nums2 = sorted(nums)
        print(nums2)
        for i in range(len(nums2)-1, -1, -1):
            n = nums2[i]
            print(nums2[i])
            if k==1:
                return n
            else:
                k -= 1

Solution.findKthLargest(1, [3,2,3,1,2,4,5,5,6], 4)
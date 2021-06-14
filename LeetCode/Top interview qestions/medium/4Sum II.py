class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        result = 0
        dd = dict()
        for n1 in nums1:
            for n2 in nums2:
                s = n1+n2
                if s in dd:
                    dd[s] = dd[s]+1
                else:
                    dd[s] = 1
                
        for n3 in nums3:
            for n4 in nums4:
                s = n3 + n4
                if -s in dd:
                    result += dd[-s]
                    
        return result
                        
        # for문 안돌리고 map으로 푸는 방법
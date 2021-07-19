import heapq

class Solution:
    def maxSlidingWindow(self, nums, k):
        pq = []
        res = []
        
        for i,n in enumerate(nums):
            if i+1 < k:
                heapq.heappush(pq, (-n, i))
            else:
                heapq.heappush(pq, (-n, i))
                x, idx = Solution.find_max(1, pq, i-k+1)
                res.append(-x)
                heapq.heappush(pq, (x, idx))
        print(res)
        return res
                
                
    def find_max(self, pq, start):
        while True:
            x, idx = heapq.heappop(pq)
            
            if idx >= start: # 창문의 첫번째 인덱스 기준 = start, 스타트보다만 뒤에 있으면 되니까 + 창문 바깥꺼는 아직 힙에 들어오지도 못함
                return x, idx
        
Solution.maxSlidingWindow(1, [9,10,9,-7,-4,-8,2,-6], 5)
        
import heapq

class MedianFinder(object):

    def __init__(self):
        self.s = 0
        self.l = 0
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num):
        self.s += num
        self.l += 1
        
        heapq.heappush(self.maxheap, num)
        temp = heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, -temp)
        if len(self.maxheap)<len(self.minheap):
            temp = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -temp)
        
    def findMedian(self):
        val1 = self.maxheap[0]
        print('val1: ', val1)
        if self.l>1:
            val2 = self.minheap[0] * -1
            print('val2: ', val2)
        if self.l%2==1:
            return float(val1)
        return float(val1+val2)/float(2)
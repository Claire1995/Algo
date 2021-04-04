
class MyCircularQueue:
    def __init__(self, k):
        self.q = list()
        self.k = k
        
    def enQueue(self, value):
        if len(self.q) < self.k:
            self.q.append(value)
            return True
        else:
            return False
        

    def deQueue(self):
        if self.q:
            del self.q[0]
            return True
        else:
            return False
            
        

    def Front(self):
        if self.q:
            return self.q[0]
        else:
            return -1
        

    def Rear(self):
        if self.q:
            return self.q[len(self.q)-1]
        else:
            return -1
        

    def isEmpty(self):
        if self.q:
            return False
        else:
            return True
        

    def isFull(self):
        if len(self.q) == self.k:
            return True
        else:
            return False   
        
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
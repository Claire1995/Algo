class MinStack(object):
    
    def __init__(self):
        self.st = list()
        self.mini = None
        

    def push(self, val):
        self.st.append(val)
        if self.mini is None:
            self.mini = val
        else:
            if self.mini > val:
                self.mini = val

    def pop(self):
        temp = self.st[len(self.st)-1]
        del self.st[len(self.st)-1]
        if self.mini == temp:
            if len(self.st)>0:
                self.mini = min(self.st)
            else:
                self.mini = None
            
        return temp
        

    def top(self):
        return self.st[len(self.st)-1]
        

    def getMin(self):
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# Definition for a binary tree node.
from collections import deque

class Codec:
    
    def __init__(self):
        self.output = ''

    def recursion(self, root):
        if root:
            if root.left:
                self.output += str(root.left.val)+'/' 
            Codec.recursion(self, root.left)
            if root.right:
                self.output += str(root.right.val)+'/'    
            Codec.recursion(self, root.right)
        else:
            self.output += 'null'+'/'
    
    def serialize(self, root):
        if root:
            self.output += str(root.val)+'/'
            Codec.recursion(self, root)
        return self.output

    def recursion2(self, root, d):
        if d:
            temp = d.popleft()
            if temp!='null':
                root.left = TreeNode(int(temp))
                Codec.recursion2(self, root.left, d)
            temp = d.popleft()
            if temp!='null':
                root.right = TreeNode(int(temp))
                Codec.recursion2(self, root.right, d)
            
            
    def deserialize(self, data):
        d = deque(list(data.split('/')))
        print(d)
        temp = d.popleft()
        if temp != '':
            root = TreeNode(int(temp))
            Codec.recursion2(self, root, d)
        else:
            return []
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
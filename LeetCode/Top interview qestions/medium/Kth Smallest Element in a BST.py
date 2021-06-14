from collections import deque
        
class Solution(object):
    def recursive(self, vals, root):
        if root.right:
            Solution.recursive(self, vals, root.right)
        vals.append(root)
        if root.left:
            Solution.recursive(self, vals, root.left)
        
        
    def kthSmallest(self, root, k):
        vals = deque()
        Solution.recursive(self, vals, root)
        answer = -1
        cnt = 0
        
        while vals:
            temp = vals.pop()
            
            answer = temp.val
            cnt += 1
            if cnt==k:
                break
            
        return answer

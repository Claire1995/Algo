# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recursive(self, ltree, rtree):
        
        if ltree is None or rtree is None:
            if ltree is None and rtree is None:
                return True
            else:
                return False
        
        if ltree.val != rtree.val:
            return False
        
        return Solution.recursive(self, ltree.right, rtree.left) and Solution.recursive(self, ltree.left, rtree.right)
        
    def isSymmetric(self, root):
        ltree = root.left
        rtree = root.right
        
        return Solution.recursive(self, ltree, rtree)
        
        
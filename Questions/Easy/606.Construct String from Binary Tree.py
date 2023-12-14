# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        string = ""
        if root:
            string +=   str(root.val) 
            if root.left or root.right:
                string += '(' + self.tree2str(root.left) +')'
            if root.right :
                string += '(' + self.tree2str(root.right) +')'
        return string

# 修剪树，在不损失1的情况下尽可能的把0去掉


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == 0:
            if root.left:
                root.left = self.pruneTree(root.left)
            if root.right:
                root.right = self.pruneTree(root.right)
            if not root.left and not root.right:
                return None
        else:
            if root.left:
                root.left = self.pruneTree(root.left)
            if root.right:
                root.right = self.pruneTree(root.right)
        return root

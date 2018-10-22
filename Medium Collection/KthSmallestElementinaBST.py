# Definition for a binary tree node.
# 解法1，简单解法，速度不快。用二叉搜索树将数从大到小排列好，取前k个数输出

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        self.helper(root, res)
        return res[k-1]

    def helper(self, root, res):
        if root.left:
            self.helper(root.left, res)
        res.append(root.val)
        if root.right:
            self.helper(root.right, res)

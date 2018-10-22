# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q = []
        flag = 1
        q.append(root)
        while q:
            cur = []
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag == 1:
                res.append(list(cur))
            else:
                res.append(list(cur[::-1]))
            flag *= -1
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 判断两颗树的叶子节点是否相同
# 使用 yield



class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)
        return list(dfs(root1)) == list(dfs(root2))




class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.root1leaves = []
        self.root2leaves = []
        self.traveltree1(root1)
        self.traveltree2(root2)
        return self.root1leaves == self.root2leaves

    def traveltree1(self, node):
        if not node:
            return
        if node.left:
            self.traveltree1(node.left)
        if node.right:
            self.traveltree1(node.right)
        if not node.left and not node.right:
            self.root1leaves.append(node.val)
        return

    def traveltree2(self, node):
        if not node:
            return
        if node.left:
            self.traveltree2(node.left)
        if node.right:
            self.traveltree2(node.right)
        if not node.left and not node.right:
            self.root2leaves.append(node.val)
        return

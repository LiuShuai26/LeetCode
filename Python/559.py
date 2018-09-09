"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        q, level = [root], 0
        while any(q):
            level += 1
            q = [child for node in q for child in node.children if child]
        return level

        # newQ = []  # We create new empty queue for next iteration
        # for node in q:  # For current nodes in q
        #     for child in node.children:  # For N-ary tree, these are child nodes in node.children
        #         if child:  # We should append it if it is not None or empty nodde in other words!
        #             newQ.append = child  # We append it
        # q = newQ





# dfs
class Solution0(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(node) for node in root.children) + 1


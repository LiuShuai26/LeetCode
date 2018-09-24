# 给一个数组，求一个树。
# 树的根节点是数组中的最大值，数组里除去这个值
# 同样，节点的左孩子和右孩子也是数组中的最大值


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        root, maxi = TreeNode(max(nums)), nums.index(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:maxi])  # 最大值左边的归左子树
        root.right = self.constructMaximumBinaryTree(nums[maxi+1:])  # 最大值左边的归右子树
        return root  # 最后返回树根

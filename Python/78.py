# 给一个不同数字的集合，求所有可能的子集
# 用dfs探索每一个可能的子集
# dfs需要一个数组记录该位置是否被访问
# 需要step变量记录当前位置


class Solution:

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.book = [0] * len(nums)
        self.result = [[]]
        self.dfs(nums, self.book, 0)
        return self.result

    def dfs(self, nums, book, step):
        if step < 0:
            return
        if step >= len(nums):
            return
        book[step] = 1
        subset = (n for b, n in zip(book, nums) if b == 1)
        self.result.append(list(subset))
        self.dfs(nums, book, step+1)
        book[step] = 0
        self.dfs(nums, book, step+1)

s = Solution()
r = s.subsets([1, 2, 3])
print(r)

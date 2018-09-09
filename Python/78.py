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

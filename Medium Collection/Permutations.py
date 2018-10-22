class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        book = [0 for _ in range(len(nums))]
        self.helper(res, nums, book, [], 0)
        return res

    def helper(self, res, nums, book, cur, step):
        if step == len(nums):
            res.append(list(cur))
            return
        for i in range(len(nums)):
            if book[i] == 0:
                cur.append(nums[i])
                book[i] = 1
                self.helper(res, nums, book, cur, step+1)
                cur.remove(nums[i])
                book[i] = 0


s = Solution()
print(s.permute([1, 2, 3]))

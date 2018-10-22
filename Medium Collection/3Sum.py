class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
















class SolutionTLE:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        book = [0] * len(nums)
        res = []
        self.dfs(res, book, [], 0, 0, 0, nums)
        return res

    def dfs(self, res, book, possible, sumv, step, start, nums):
        if step == 3:
            if sumv == 0:
                if sorted(possible) not in res:
                    res.append(sorted(possible))
        else:
            for i in range(start, len(nums)):
                if book[i] == 0:
                    possible.append(nums[i])
                    sumv += nums[i]
                    book[i] = 1
                    step += 1
                    self.dfs(res, book, possible, sumv, step, i+1, nums)
                    sumv -= nums[i]
                    possible.remove(nums[i])
                    book[i] = 0
                    step -= 1


s = Solution()
print(s.threeSum([-9,-14,-3,2,0,-11,-5,11,5,-5,4,-4,5,-15,14,-8,-11,10,-6,1,-14,-12,-13,-11,9,-7,-2,-13,2,2,-15,1,3,-3,-12,-12,1,-2,6,14,0,-4,-13,-10,-12,8,-2,-8,3,-1,8,4,-6,2,1,10,2,14,4,12,1,4,-2,11,9,-7,6,-13,7,-3,8,14,8,10,12,11,-4,-13,10,14,1,-4,-4,2,5,4,-11,-7,3,8,-10,11,-11,-5,7,13,3,-2,8,-13,2,1,9,-12,-11,6]))

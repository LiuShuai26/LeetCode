# 数组a，1 ≤ a[i] ≤ n (n = size of array)
# 数组中有的元素出现了一次，有的出现了两次。输出出现两次的数字
# 利用数组中的数字不超过数组大小的特点，可以*把每个数字和数组位置对应起来*
# 每访问一个数字，找到这个数字对应位置的数字，将其加负号，
# 如果该位置数字已经是负数了，则说明该位置对应的数字已经出现过一次了，加入到结果数组


class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                result.append(idx+1)
            nums[idx] *= -1
        return result


s = Solution()
print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))

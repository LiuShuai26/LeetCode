class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]*(num+1)
        for i in range(1, num+1):
            result[i] = result[i >> 1] + (i&1)
        return result

s = Solution()
print(s.countBits(5))

# 0 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111

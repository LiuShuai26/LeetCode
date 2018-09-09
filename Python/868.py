class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        n_str = bin(N)[2:]
        result = 0
        first = True
        for i in range(0, len(n_str)):
            if n_str[i] == '1' and first:
                low = i
                first = False
            elif n_str[i] == '1' and not first:
                high = i
                if high - low > result:
                    result = high - low
                low = high
        return result


s = Solution()
print(s.binaryGap(22))

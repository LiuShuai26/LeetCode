class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #  babad
        maxlen = 0
        res = ''
        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > maxlen:
                maxlen = len(tmp)
                res = tmp
            tmp = self.helper(s, i, i+1)
            if len(tmp) > maxlen:
                maxlen = len(tmp)
                res = tmp
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

s = Solution()
print(s.longestPalindrome('a'))
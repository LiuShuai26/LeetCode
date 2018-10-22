class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        appear = []  # dvdfkdsz ddvz
        for i in range(len(s)):
            if s[i] in appear:
                if len(appear) > res:
                    res = len(appear)
                appear = appear[appear.index(s[i])+1:]
                appear.append(s[i])
            else:
                appear.append(s[i])
        if len(appear) > res:
            res = len(appear)
        return res


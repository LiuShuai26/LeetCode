# 返回两个不同数组中各不相同的词
# 解：所有的词放一起，返回出现一次的词


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        result = []
        words = A.split(' ')
        words += B.split(' ')
        for word in words:
            if words.count(word) == 1:
                result.append(word)
        return result
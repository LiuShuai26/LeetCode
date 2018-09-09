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
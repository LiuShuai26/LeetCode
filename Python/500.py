# 简单题


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        qwe = 'qwertyuiop'
        asd = 'asdfghjkl'
        zxc = 'zxcvbnm'
        result = []
        for word in words:
            word_lower = word.lower()
            flag = True
            if word_lower[0] in qwe:
                for w in word_lower:
                    if w not in qwe:
                        flag = False
            elif word_lower[0] in asd:
                for w in word_lower:
                    if w not in asd:
                        flag = False
            elif word_lower[0] in zxc:
                for w in word_lower:
                    if w not in zxc:
                        flag = False
            if flag:
                result.append(word)
        return result




class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s[::-1].split(' ')[::-1])





class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        s = s[::-1]
        for i in reversed(s.split(' ')):
            result = result + i + ' '
        return result[:-1]
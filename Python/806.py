

class Solution(object):
    def numberOfLines(self, widths, S):
        lines, width = 1, 0
        for c in S:
            w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w
        return lines, width





class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        w = 0
        line = 1
        for s in S:
            width = widths[alphabet.index(s)]
            if w + width > 100:
                w = 0
                line += 1
            w += width
        return [line, w]
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(n, n, '', res)
        return res

    def helper(self, left, right, string, res):
        if right < left:
            return
        if not left and not right:
            res.append(string)
        if left:
            self.helper(left-1, right, string+'(', res)
        if right:
            self.helper(left, right-1, string+')', res)

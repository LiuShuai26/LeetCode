# 将字符串T按照S中字母顺序排序


class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        result = []
        for s in S:
            result.append(s*T.count(s))  # 遍历S 当前字母乘以在T中出现的次数
        for t in T:
            if t not in S:
                result.append(t)
        return ('').join(result)

from functools import reduce
from operator import mul


class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]  # 如果字典中无key，返回第二个参数[]
        return d.values()


class Solution1:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                  47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        res = {}
        for str_ in strs:
            key = reduce(mul, [primes[ord(c) - ord('a')] for c in str_]) if str_ else ""
            res.setdefault(key, []).append(str_)
        return list(res.values())


class Solution2:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        group = []
        for str in strs:
            strlist = list(str)
            strlist = sorted(strlist)
            strsorted = ('').join(strlist)
            if strsorted not in group:
                group.append(strsorted)
                res.append([str])
            else:
                res[group.index(strsorted)].append(str)
        return res

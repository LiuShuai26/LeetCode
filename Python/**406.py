# 假设你有一个随机列表关于人站在一个队里
# 每个人被表示为一对数字(h, k)h代表这个人的高度，看代表这个人前面有几个人比他高
# 写一个算法重新排列这个队
# 排列前：[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
# 排列后：[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
#


class Solution(object):
    def reconstructQueue(self, people):
        if not people:
            return []
        peopledct, height, res = {}, [], []

        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],

        height.sort()

        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])
        return res


s = Solution()
print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))

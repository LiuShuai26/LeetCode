# 简单并查集，并查集数组中值与下标相等的数量为圈子的数量（圈子内的人有同一个祖先）


class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.father = [0] * len(M)
        for i in range(len(M)):
            self.father[i] = i
        self.count = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    self.Union(i, j)
        for i in range(len(M)):
            if self.father[i] == i:
                self.count += 1

        return self.count


    def Find(self, x):
        while(x != self.father[x]):
            x = self.father[x]
        return x

    def Union(self, a, b):
        fa = self.Find(a)
        fb = self.Find(b)
        if fa != fb:
            self.father[fa] = fb

M = [[1,1,0],
 [1,1,0],
 [0,0,1]]
s = Solution()
x = s.findCircleNum(M)
print(x)
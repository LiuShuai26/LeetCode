class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        steps = 1
        times = 2
        n = -1
        count = 0
        result = [[r0, c0]]
        while True:
            if len(result) >= R*C:
                break
            n *= -1
            for i in range(times):
                if i == 0:
                    fi = 0
                    fj = 1*n
                else:
                    fi = 1*n
                    fj = 0
                for _ in range(steps):
                    r0 += fi
                    c0 += fj
                    if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                        result.append([r0, c0])
            steps += 1
        return result

s = Solution()
print(s.spiralMatrixIII(5, 6, 1, 4))

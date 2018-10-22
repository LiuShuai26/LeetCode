class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        zeroi = []
        zeroj = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroi.append(i)
                    zeroj.append(j)
                    for m in range(0, i):
                        matrix[m][j] = 0
                    for n in range(0, j):
                        matrix[i][n] = 0
                if i in zeroi:
                    matrix[i][j] = 0
                if j in zeroj:
                    matrix[i][j] = 0
        return matrix


s = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(s.setZeroes(matrix))

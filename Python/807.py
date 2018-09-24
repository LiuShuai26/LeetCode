# 基础技巧题


class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        gridOriginal = [sum(row) for row in grid]
        originalSum = sum(gridOriginal)
        maxUpToDown = []
        for i in range(0, len(grid[0])):
            maxUpToDown.append(max([row[i] for row in grid]))
        maxLeftToRight = []
        for row in grid:
            maxLeftToRight.append(max(row))
        for i in range(0, len(grid[0])):
            for j in range(0, len(grid)):
                grid[i][j] = min(maxUpToDown[i], maxLeftToRight[j])
        grid = [sum(row) for row in grid]
        return sum(grid) - originalSum

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.helper(i, j, grid)
        return res

    def helper(self, m, n, grid):
        grid[m][n] = '0'
        if m+1 < len(grid) and grid[m+1][n] == '1':
            self.helper(m+1, n, grid)
        if m-1 >= 0 and grid[m-1][n] == '1':
            self.helper(m-1, n, grid)
        if n+1 < len(grid[0]) and grid[m][n+1] == '1':
            self.helper(m, n+1, grid)
        if n-1 >= 0 and grid[m][n-1] == '1':
            self.helper(m, n-1, grid)

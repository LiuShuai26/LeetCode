# 动态规划
# dp[i][j]为局i到j第一个玩家比第二个玩家领先的分数
# 在情况i到i+d中，可以取第一个值或者取最后一个值
# 如果取piles[i]，对手在i+1到i+d之间得到的最大分数是dp[i+1][i+d]，
# 所以你的领先分数为piles[i]-dp[i+1][i+d]


class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0] * n for i in range(n)]  # 初始化一个值为0的n*n的二维数组
        for i in range(n):
            dp[i][i] = piles[i]
        for d in range(1, n):
            for i in range(n-d):
                dp[i][i+d] = max(piles[i]-dp[i+1][i+d], piles[i+d]-dp[i][i+d-1])
        return dp[0][-1] > 0

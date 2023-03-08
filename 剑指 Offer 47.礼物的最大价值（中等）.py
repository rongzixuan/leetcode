"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:
输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 
提示：
0 < grid.length <= 200
0 < grid[0].length <= 200

"""

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1] + grid[i][j], dp[i + 1][j] + grid[i][j], dp[i + 1][j + 1])
        return dp[m][n]


        # 方法二：动态规划
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(n)
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n + 1) for _ in range(2)]
        for i in range(m):
            for j in range(n):
                dp[(i + 1) & 1][j + 1] = max(dp[i & 1][j + 1] + grid[i][j], dp[(i + 1) & 1][j] + grid[i][j], dp[(i + 1) & 1][j + 1])
        return dp[m & 1][n]



        


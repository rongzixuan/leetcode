"""
给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。
给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 109 + 7 取余 后的结果。
"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(m * n * maxMove)
        # 空间复杂度：o(m * n * maxMove)
        if maxMove == 0:
            return 0
            
        count = 0
        MOD = 10 ** 9 + 7
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dp = [[[0] * (maxMove+1) for _ in range(n)] for _ in range(m)]

        # 初始化
        for di in directions:
            if 0 <= (startRow + di[0]) < m and 0 <= (startColumn + di[1]) < n:
                #print(startRow+i, startColumn+j)
                dp[startRow+di[0]][startColumn+di[1]][1] = 1
                #print(dp)
            else:
                count += 1
        #print(dp)
        #print(count)

        for k in range(0, maxMove):
            for i in range(m):
                for j in range(n):                             
                    for di in directions:
                        if 0 <= i+di[0] < m and 0 <= j+di[1] < n:
                            dp[i+di[0]][j+di[1]][k+1] += dp[i][j][k]
                        else:
                            count += dp[i][j][k]
        #print(dp)

        return count % MOD




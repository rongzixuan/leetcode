"""
在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。
象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。

每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。
骑士继续移动，直到它走了 k 步或离开了棋盘。
返回骑士在棋盘停止移动后仍留在棋盘上的概率 。

示例 1：
输入: n = 3, k = 2, row = 0, column = 0
输出: 0.0625
解释: 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
在每一个位置上，也有两种移动可以让骑士留在棋盘上。
骑士留在棋盘上的总概率是0.0625。

示例 2：
输入: n = 1, k = 0, row = 0, column = 0
输出: 1.00000
 
提示:
1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n

"""


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:


        # 方法一：动态规划 + 广度优先搜索
        # 时间复杂度：O(n * n * k)
        # 空间复杂度：O(n * n * k)
        # dp[k][i][j]表示第k步时落在(i, j)的概率
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]   
        dp[0][row][column] = 1
        #print(dp)
        place1 = {(row, column)}

        for i in range(1, k + 1):
            place2 = set()
            for r, c in place1:
                prob = dp[i - 1][r][c]
                for new_r, new_c in [(r - 2, c - 1), (r - 1, c - 2), (r + 1, c - 2), (r + 2, c - 1), (r + 2, c + 1), (r + 1, c + 2), (r - 1, c + 2), (r - 2, c + 1)]:
                    if 0 <= new_r < n and 0 <= new_c < n:
                        dp[i][new_r][new_c] += prob / 8
                        place2.add((new_r, new_c))
            place1 = place2

        #print(dp)
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += dp[k][i][j]
        return ans


        # 方法二：动态规划 + 广度优先搜索2
        # 时间复杂度：O(n * n * k)
        # 空间复杂度：O(n * n * k)
        # dp[k][i][j]表示从(i, j)开始，第k步时落在(i, j)的概率
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)] 
        #dp[0][row][column] = 1

        for step in range(0, k + 1):
            for r in range(n):
                for c in range(n):
                    if step == 0:
                        dp[step][r][c] = 1
                    else:
                        for new_r, new_c in [(r - 2, c - 1), (r - 1, c - 2), (r + 1, c - 2), (r + 2, c - 1), (r + 2, c + 1), (r + 1, c + 2), (r - 1, c + 2), (r - 2, c + 1)]:
                            if 0 <= new_r < n and 0 <= new_c < n:
                                dp[step][new_r][new_c] += dp[step - 1][r][c] / 8
                                
        print(dp)
        return dp[k][row][column]






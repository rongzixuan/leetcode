"""
在一个 n x n 的矩阵 grid 中，除了在数组 mines 中给出的元素为 0，其他每个元素都为 1。mines[i] = [xi, yi]表示 grid[xi][yi] == 0
返回  grid 中包含 1 的最大的 轴对齐 加号标志的阶数 。如果未找到加号标志，则返回 0 。

一个 k 阶由 1 组成的 “轴对称”加号标志 具有中心网格 grid[r][c] == 1 ，以及4个从中心向上、向下、向左、向右延伸，长度为 k-1，由 1 组成的臂。注意，只有加号标志的所有网格要求为 1 ，别的网格可能为 0 也可能为 1 。

示例 1：
输入: n = 5, mines = [[4, 2]]
输出: 2
解释: 在上面的网格中，最大加号标志的阶只能是2。一个标志已在图中标出。

示例 2：
输入: n = 1, mines = [[0, 0]]
输出: 0
解释: 没有加号标志，返回 0 。
 
提示：
1 <= n <= 500
1 <= mines.length <= 5000
0 <= xi, yi < n
每一对 (xi, yi) 都 不重复

"""

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:


        # 方法一：动态规划（错误）
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        mines_set = set()
        #print(mines)
        dp = [[[1] * 4 for _ in range(n)] for _ in range(n)]
        #print(dp)
        for i, j in mines:
            for k in range(4):
                dp[i][j][k] = 0
            mines_set.add((i, j))

        for i, j in product(range(n), range(n)):
            #print(i, j)
            if (i, j) not in mines_set:
                if i - 1 >= 0:
                    dp[i][j][2] = dp[i - 1][j][2] + 1
                if i + 1 < n:
                    dp[i][j][0] = dp[i + 1][j][0] + 1
                if j - 1 >= 0:
                    dp[i][j][3] = dp[i][j - 1][3] + 1
                if j + 1 < n:
                    dp[i][j][1] = dp[i][j + 1][1] + 1
            else:
                dp[i][j][0] = 0
                dp[i][j][1] = 0
                dp[i][j][2] = 0
                dp[i][j][3] = 0
        print(dp)
        
        dp_t = [[0 for _ in range(n)] for _ in range(n)]
        #print('dp_t:', dp_t)
        for i, j in product(range(n), range(n)):
            dp_t[i][j] = min([dp[i][j][k] for k in range(4)])
        ans = 0
        for i, j in product(range(n), range(n)):
            ans = max(ans, dp_t[i][j])
        return ans


        # 方法二：动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        mines_set = set()
        #print(mines)
        dp = [[[1] * 4 for _ in range(n)] for _ in range(n)]
        #print(dp)
        for i, j in mines:
            for k in range(4):
                dp[i][j][k] = 0
            mines_set.add((i, j))

        for i, j in product(range(n), range(n)):
            #print(i, j)
            if (i, j) not in mines_set:
                if i - 1 >= 0:
                    dp[i][j][2] = dp[i - 1][j][2] + 1
                if i + 1 < n:
                    dp[i][j][0] = dp[i + 1][j][0] + 1
                if j - 1 >= 0:
                    dp[i][j][3] = dp[i][j - 1][3] + 1
                if j + 1 < n:
                    dp[i][j][1] = dp[i][j + 1][1] + 1
            else:
                dp[i][j][0] = 0
                dp[i][j][1] = 0
                dp[i][j][2] = 0
                dp[i][j][3] = 0
        
        for i, j in product(range(n - 1, -1, -1), range(n - 1, -1, -1)):
            #print(i, j)
            if (i, j) not in mines_set:
                if i - 1 >= 0:
                    dp[i][j][2] = dp[i - 1][j][2] + 1
                if i + 1 < n:
                    dp[i][j][0] = dp[i + 1][j][0] + 1
                if j - 1 >= 0:
                    dp[i][j][3] = dp[i][j - 1][3] + 1
                if j + 1 < n:
                    dp[i][j][1] = dp[i][j + 1][1] + 1
            else:
                dp[i][j][0] = 0
                dp[i][j][1] = 0
                dp[i][j][2] = 0
                dp[i][j][3] = 0
        #print(dp)
        
        dp_t = [[0 for _ in range(n)] for _ in range(n)]
        #print('dp_t:', dp_t)
        for i, j in product(range(n), range(n)):
            dp_t[i][j] = min([dp[i][j][k] for k in range(4)])
        ans = 0
        for i, j in product(range(n), range(n)):
            ans = max(ans, dp_t[i][j])
        return ans


        # 方法三：动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        dp = [[n] * n for _ in range(n)]
        banned = set(map(tuple, mines))
        for i in range(n):
            # left
            count = 0
            for j in range(n):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
            # right
            count = 0
            for j in range(n - 1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
        for j in range(n):
            # up
            count = 0
            for i in range(n):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
            # down
            count = 0
            for i in range(n - 1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
        return max(map(max, dp))





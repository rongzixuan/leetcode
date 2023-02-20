"""
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。

示例 1：
输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9

示例 2：
输入：grid = [[1,1,0,0]]
输出：1

提示：
1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] 为 0 或 1

"""

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:


        # 方法一：前缀和
        # 时间复杂度：O(m * n * min(m, n))
        # 空间复杂度：O(m * n)
        m, n = len(grid), len(grid[0])
        pre_c = [[0] * (n + 1) for _ in range(m + 1)]
        pre_r = [[0] * (n + 1) for _ in range(m + 1)]
        #print(pre_c)

        for i in range(m):
            pre = 0
            for j in range(n):
                if grid[i][j] == 1:
                    pre += 1
                pre_r[i + 1][j + 1] = pre
        #print(pre_r)

        for j in range(n):
            pre = 0
            for i in range(m):
                if grid[i][j] == 1:
                    pre += 1
                pre_c[i + 1][j + 1] = pre
        #print(pre_c)

        ans = 0
        for i, j in product(range(m), range(n)):
            #print('i, j:', i, j)
            length = min(m - i, n - j)
            #print('length:', length)
            for k in range(0, length):
                #print('k:', k)
                if pre_c[i + k + 1][j + 1] - pre_c[i][j + 1] == k + 1 \
                and pre_c[i + k + 1][j + k + 1] - pre_c[i][j + k + 1] == k + 1 \
                and pre_r[i + 1][j + k + 1] - pre_r[i + 1][j] == k +1 \
                and pre_r[i + k + 1][j + k + 1] - pre_r[i + k + 1][j] == k + 1:
                    ans = max(ans, k + 1)
        return ans**2


        # 方法二：前缀和
        # 时间复杂度：O(m * n * min(m, n))
        # 空间复杂度：O(m * n)
        m, n = len(grid), len(grid[0])
        down = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    down[i][j] = down[i + 1][j] + 1 if i + 1 < m else 1
                    right[i][j] = right[i][j + 1] + 1 if j + 1 < n else 1
        for k in range(min(m, n), 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if down[i][j] >= k and right[i][j] >= k and right[i + k - 1][j] >= k and down[i][j + k - 1] >= k:
                        return k * k
        return 0






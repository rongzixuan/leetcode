"""
在 n x n 的网格 grid 中，我们放置了一些与 x，y，z 三轴对齐的 1 x 1 x 1 立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。

现在，我们查看这些立方体在 xy 、yz 和 zx 平面上的投影。

投影 就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回 所有三个投影的总面积 。


示例 1：
输入：[[1,2],[3,4]]
输出：17
解释：这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。

示例 2:
输入：grid = [[2]]
输出：5

示例 3：
输入：[[1,0],[0,2]]
输出：8

提示：
n == grid.length == grid[i].length
1 <= n <= 50
0 <= grid[i][j] <= 50

"""


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:


        # 方法一：数学
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        #print(grid)
        #print(*grid)
        #print(zip(*grid))
        n = len(grid)
        #print([grid[i][j] for i in range(n) for j in range(n)])  

        ans = 0
        ans += sum([grid[i][j] > 0 for i in range(n) for j in range(n)]) # 俯视图
        #print(ans)

        ans += sum([max(grid[i]) for i in range(n)])  # 侧视图
        #print(ans)

        import numpy as np
        #print(np.max(grid, axis=0))
        #print(np.max(grid, axis=1))
        ans += int(sum(np.max(grid, axis=0)))
        #print(ans)

        return ans


        # 方法二：数学
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        xyArea = sum(v > 0 for row in grid for v in row)
        yzArea = sum(map(max, zip(*grid)))  # 注意这里为 O(n) 空间复杂度，改为下标枚举则可以 O(1)
        zxArea = sum(map(max, grid))
        return xyArea + yzArea + zxArea






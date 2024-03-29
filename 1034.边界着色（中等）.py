"""
给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color 。网格中的每个值表示该位置处的网格块的颜色。

两个网格块属于同一 连通分量 需满足下述全部条件：
两个网格块颜色相同
在上、下、左、右任意一个方向上相邻

连通分量的边界 是指连通分量中满足下述条件之一的所有网格块：
在上、下、左、右四个方向上与不属于同一连通分量的网格块相邻
在网格的边界上（第一行/列或最后一行/列）

请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色，并返回最终的网格 grid 。

示例 1：
输入：grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
输出：[[3,3],[3,2]]

示例 2：
输入：grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
输出：[[1,3,3],[2,3,3]]

示例 3：
输入：grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
输出：[[2,2,2],[2,1,2],[2,2,2]]
 
提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j], color <= 1000
0 <= row < m
0 <= col < n

"""


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:


        # 方法一：广度优先搜索
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        m, n = len(grid), len(grid[0])
        init_color = grid[row][col]
        if init_color == color:
            return grid

        queue = [(row, col)]
        visited = [[False] * n for _ in range(m)]
        visited[row][col] = True
        while queue:
            row, col = queue.pop(0)
            if row == 0 or col == 0 or row == m-1 or col == n-1:
                grid[row][col] = color
            for new_row, new_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= new_row < m and 0 <= new_col < n:
                    if visited[new_row][new_col] == False and grid[new_row][new_col] != init_color:
                        grid[row][col] = color
                    elif visited[new_row][new_col] == False and grid[new_row][new_col] == init_color:
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col))

        return grid


        # 方法二：深度优先搜索
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        m, n = len(grid), len(grid[0])
        init_color = grid[row][col]
        if init_color == color:
            return grid

        visited = [[False] * n for _ in range(m)]
        visited[row][col] = True

        def dfs(row, col):
            if row == 0 or col == 0 or row == m-1 or col == n-1:
                grid[row][col] = color
            for new_row, new_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= new_row < m and 0 <= new_col < n:
                    if visited[new_row][new_col] == False and grid[new_row][new_col] != init_color:
                        grid[row][col] = color
                    elif visited[new_row][new_col] == False and grid[new_row][new_col] == init_color:
                        visited[new_row][new_col] = True
                        dfs(new_row, new_col)

        dfs(row, col)
        return grid




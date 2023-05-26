"""
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：
路径途经的所有单元格的值都是 0 。
路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。

畅通路径的长度 是该路径途经的单元格总数。

示例 1：
输入：grid = [[0,1],[1,0]]
输出：2

示例 2：
输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
输出：4

示例 3：
输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
输出：-1
 
提示：
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] 为 0 或 1

"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:


        # 方法一：广度优先搜索
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)        
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        queue = [(0, 0, 1)]
        used = set((0, 0))
        while queue:
            for _ in range(len(queue)):
                x, y, step = queue.pop(0)
                if x == n - 1 and y == n - 1:
                    return step
                for new_x, new_y in [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1], [x, y + 1], [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]:
                    if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in used and grid[new_x][new_y] == 0:
                        used.add((new_x, new_y))
                        queue.append((new_x, new_y, step + 1))
        return -1





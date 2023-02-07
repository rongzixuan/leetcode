"""
给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。

一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。

返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。

示例 1：
输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。

示例 2：
输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
输出：0
解释：所有 1 都在边界上或可以到达边界。
 
提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] 的值为 0 或 1

"""


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:


        # 方法一：广度优先搜索
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        m, n = len(grid), len(grid[0])

        def bfs(i, j):
            from collections import deque
            queue = deque()
            queue.append((i, j))
            grid[i][j] = 2
            area = 1
            fd_falg = False

            while queue:
                i, j = queue.popleft()
                for new_i, new_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:
                        queue.append((new_i, new_j))
                        grid[new_i][new_j] = 2
                        area += 1
                    elif new_i == - 1 or new_i == m or new_j == -1 or new_j == n:
                        #print(new_i, new_j)
                        fd_falg = True
            #print('area:', area)
            return 0 if fd_falg else area

        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area += bfs(i, j)
        return area


        # 方法二：深度优先搜索（栈）
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            from collections import deque
            stack = deque()
            stack.append((i, j))
            grid[i][j] = 2
            area = 1
            fd_falg = False

            while stack:
                i, j = stack.pop()
                for new_i, new_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:
                        stack.append((new_i, new_j))
                        grid[new_i][new_j] = 2
                        area += 1
                    elif new_i == - 1 or new_i == m or new_j == -1 or new_j == n:
                        #print(new_i, new_j)
                        fd_falg = True
            #print('area:', area)
            return 0 if fd_falg else area

        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area += dfs(i, j)
        return area


        # 方法三：深度优先搜索（递归）
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        m, n = len(grid), len(grid[0])

        def dfs(i, j, father_flag):
            grid[i][j] = 2
            tmp_flag = True if father_flag else False
            tmp_area = 1

            for new_i, new_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:
                    grid[new_i][new_j] = 2
                    child_flag, child_area = dfs(new_i, new_j, tmp_flag)
                    #print('new_i, new_j, child_area, child_flag:', new_i, new_j, child_area, child_flag)
                    if child_flag:
                        tmp_flag = True
                    else:
                        tmp_area += child_area
                elif new_i == - 1 or new_i == m or new_j == -1 or new_j == n:
                    #print(new_i, new_j)
                    tmp_flag = True
            #print('area:', area)
            if tmp_flag: 
                return True, 0  
            else:
                #print('i, j, tmp_area:', i, j, tmp_area)
                return False, tmp_area

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    flag, area = dfs(i, j, False)
                    ans += area
        return ans





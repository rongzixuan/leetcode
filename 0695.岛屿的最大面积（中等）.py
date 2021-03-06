"""
给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        # 方法一：广度优先搜索
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        m, n = len(grid), len(grid[0])       
        max_area = 0

        for i in range(m):
            for j in range(n):

                queue = []
                area = 0
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = 2
                    
                    while queue:
                        i, j = queue.pop(0)
                        #print(i, j)
                        area += 1
                        #grid[i][j] = 2
                        for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                            if 0 <= new_i < m and 0 <= new_j < n:
                                if grid[new_i][new_j] == 1:
                                    queue.append((new_i, new_j))
                                    grid[new_i][new_j] = 2

                #print('area:', area)
                max_area = max(max_area, area)

        return max_area


        # 方法二：深度优先搜索（递归）
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        m, n = len(grid), len(grid[0])       
        max_area = 0

        def getArea(i, j):
            #area = 0
            grid[i][j] = 2
            #area += 1

            def dfs(i, j):
                area = 0
                for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= new_i < m and 0 <= new_j < n:
                        if grid[new_i][new_j] == 1:
                            grid[new_i][new_j] = 2
                            area += 1
                            area += dfs(new_i, new_j)

                return area
            
            return dfs(i, j) + 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = getArea(i, j)   
                    max_area = max(max_area, area)

        return max_area


        # 方法三：深度优先搜索（栈）
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        m, n = len(grid), len(grid[0])       
        max_area = 0

        for i in range(m):
            for j in range(n):

                stack = []
                area = 0
                if grid[i][j] == 1:
                    stack.append((i, j))
                    grid[i][j] = 2
                    
                    while stack:
                        i, j = stack.pop(-1)
                        #print(i, j)
                        area += 1
                        #grid[i][j] = 2
                        for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                            if 0 <= new_i < m and 0 <= new_j < n:
                                if grid[new_i][new_j] == 1:
                                    stack.append((new_i, new_j))
                                    grid[new_i][new_j] = 2

                #print('area:', area)
                max_area = max(max_area, area)

        return max_area




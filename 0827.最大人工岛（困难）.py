"""
给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。
返回执行此操作后，grid 中最大的岛屿面积是多少？

岛屿 由一组上、下、左、右四个方向相连的 1 形成。

示例 1:
输入: grid = [[1, 0], [0, 1]]
输出: 3
解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。

示例 2:
输入: grid = [[1, 1], [1, 0]]
输出: 4
解释: 将一格0变成1，岛屿的面积扩大为 4。

示例 3:
输入: grid = [[1, 1], [1, 1]]
输出: 4
解释: 没有0可以让我们变成1，面积依然为 4。

提示：
n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] 为 0 或 1

"""

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:


        # 方法一：深度优先搜索
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        def dfs(i, j, mark):
            #print(i, j, mark)
            tmp_area = 1
            grid[i][j] = mark
            for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == 1:
                    tmp_area += dfs(new_i, new_j, mark)
            return tmp_area  

        """@cache
        def bfs(i1, j1, mark1, i2, j2, mark2):
            queue1 = [(i1, j1)]
            used = set((i1, j1))
            used2 = set()
            edges = list()        
            while queue1:
                i, j = queue1.pop(0)
                for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= new_i < n and 0 <= new_j < n:
                        if grid[new_i][new_j] == 0:
                            edges.append((i, j, 0))
                            used2.add((i, j))
                        elif grid[new_i][new_j] == mark1 and (new_i, new_j) not in used:
                            queue1.append((new_i, new_j))
                            used.add((new_i, new_j))

            while edges:
                i, j, dist = edges.pop(0)
                for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= new_i < n and 0 <= new_j < n:
                        if grid[new_i][new_j] == mark2:
                            return dist + 1
                        elif (new_i, new_j) not in used2 and grid[new_i][new_j] == 0:
                            edges.append((new_i, new_j, dist + 1))"""

        n = len(grid)
        mark = 2
        from collections import defaultdict
        area = defaultdict(list)
        while True:
            flag = False
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        #print(i, j)
                        tmp_area = dfs(i, j, mark)
                        area[mark] = [i, j, tmp_area]
                        flag = True
                        mark += 1
            if not flag:
                break
        #print(grid)
        #print(area)
        if len(area) == 0:
            return 1

        ans = 0
        used3 = set()
        for i, j in product(range(n), range(n)):
            if grid[i][j] == 0:
                tmp = 1
                for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] != 0:
                        mark = grid[new_i][new_j]
                        #print(area[mark])
                        if mark not in used3:
                            tmp += area[mark][2]
                            used3.add(mark)
                ans = max(ans, tmp)
                used3 = set()
        return ans if ans != 0 else n * n



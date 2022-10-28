"""
给你一个大小为 n x n 的二元矩阵 grid ，其中 1 表示陆地，0 表示水域。
岛 是由四面相连的 1 形成的一个最大组，即不会与非组内的任何其他 1 相连。grid 中 恰好存在两座岛 。
你可以将任意数量的 0 变为 1 ，以使两座岛连接起来，变成 一座岛 。
返回必须翻转的 0 的最小数目。

示例 1：
输入：grid = [[0,1],[1,0]]
输出：1

示例 2：
输入：grid = [[0,1,0],[0,0,0],[0,0,1]]
输出：2

示例 3：
输入：grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
输出：1

提示：
n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] 为 0 或 1
grid 中恰有两个岛

"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:


        # 方法一：两次广度优先搜索
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(grid)
        queue1 = []
        used1 = set()
        for i, j in product(range(n), range(n)):
            if grid[i][j] == 1:
                queue1.append((i, j))
                used1.add((i, j))
                break

        while queue1:
            i, j = queue1.pop(0)
            grid[i][j] = 2
            for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == 1 and (new_i, new_j) not in used1:
                    queue1.append((new_i, new_j))
                    used1.add((new_i, new_j))
        #print(grid)

        queue2 = []
        used2 = set()
        for i, j in used1:
            queue2.append((i, j, 0))
            used2.add((i, j))
        #print(queue2)
        while queue2:
            for _ in range(len(queue2)):
                i, j, d = queue2.pop(0)
                for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] != 2 and (new_i, new_j) not in used2:
                        if grid[new_i][new_j] == 1:
                            return d
                        queue2.append((new_i, new_j, d + 1))
                        used2.add((new_i, new_j))


        # 方法二：深度优先搜索 + 广度优先搜索
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(grid)
        stack = []
        used1 = set()
        for i, j in product(range(n), range(n)):
            if grid[i][j] == 1:
                stack.append((i, j))
                used1.add((i, j))
                break

        while stack:
            i, j = stack.pop()
            grid[i][j] = 2
            for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == 1 and (new_i, new_j) not in used1:
                    stack.append((new_i, new_j))
                    used1.add((new_i, new_j))
        #print(grid)

        queue2 = []
        used2 = set()
        for i, j in used1:
            queue2.append((i, j, 0))
            used2.add((i, j))
        #print(queue2)
        while queue2:
            for _ in range(len(queue2)):
                i, j, d = queue2.pop(0)
                for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] != 2 and (new_i, new_j) not in used2:
                        if grid[new_i][new_j] == 1:
                            return d
                        queue2.append((new_i, new_j, d + 1))
                        used2.add((new_i, new_j))




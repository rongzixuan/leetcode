"""
在给定的网格中，每个单元格可以有以下三个值之一：
值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。

每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        # 方法一：广度优先搜索
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        m, n = len(grid), len(grid[0])

        queue = []   # 腐烂橘子的位置
        count1 = 0      # 新鲜橘子的个数
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count1 += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, 0))

        print(count1)
        if count1 == 0:
            return 0

        max_time = 0
        while queue:
            length = len(queue)
            i, j, time = queue.pop(0)
            max_time = time
            
            for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= new_i < m and 0 <= new_j < n:
                    if grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        count1 -= 1
                        queue.append((new_i, new_j, time+1))

        #print(count1)
        return max_time if count1 == 0 else -1

    
    
    

"""
给你一个大小为 m x n 的整数矩阵 isWater ，它代表了一个由 陆地 和 水域 单元格组成的地图。

如果 isWater[i][j] == 0 ，格子 (i, j) 是一个 陆地 格子。
如果 isWater[i][j] == 1 ，格子 (i, j) 是一个 水域 格子。

你需要按照如下规则给每个单元格安排高度：
每个格子的高度都必须是非负的。
如果一个格子是是 水域 ，那么它的高度必须为 0 。
任意相邻的格子高度差 至多 为 1 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）

找到一种安排高度的方案，使得矩阵中的最高高度值 最大 。

请你返回一个大小为 m x n 的整数矩阵 height ，其中 height[i][j] 是格子 (i, j) 的高度。如果有多种解法，请返回 任意一个 。

示例 1：
输入：isWater = [[0,1],[0,0]]
输出：[[1,0],[2,1]]
解释：上图展示了给各个格子安排的高度。
蓝色格子是水域格，绿色格子是陆地格。

示例 2：
输入：isWater = [[0,0,1],[1,0,0],[0,0,0]]
输出：[[1,1,0],[0,1,1],[1,2,2]]
解释：所有安排方案中，最高可行高度为 2 。
任意安排方案中，只要最高高度为 2 且符合上述规则的，都为可行方案。
 
提示：
m == isWater.length
n == isWater[i].length
1 <= m, n <= 1000
isWater[i][j] 要么是 0 ，要么是 1 。
至少有 1 个水域格子。

"""


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:


        # 方法一：多元广度优先搜索
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        m, n = len(isWater), len(isWater[0])
        #print(m, n)

        res = [[-1] * n for _ in range(m)]
        queue = []
        queue = deque()
        #visited = [[False] * n for _ in range(m)]
        #visited = set()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    res[i][j] = 0
                    #visited[i][j] = True
                    #visited.add((i, j))
        #print(queue)
        
        while queue:
            #i, j = queue.pop(0) 
            i, j = queue.popleft()          
            #print(i, j)
            for new_i, new_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= new_i < m and 0 <= new_j < n and res[new_i][new_j] == -1:
                    """min_ = float('inf')
                    for tmp_i, tmp_j in [(new_i + 1, new_j), (new_i - 1, new_j), (new_i, new_j + 1), (new_i, new_j - 1)]:
                        if 0 <= tmp_i < m and 0 <= tmp_j < n and (tmp_i, tmp_j) in visited:
                            min_ = min(min_, res[tmp_i][tmp_j])
                    res[new_i][new_j] = min_ + 1"""
                    res[new_i][new_j] = res[i][j] + 1
                    queue.append((new_i, new_j))
                    #visited[new_i][new_j] = True
                    #visited.add((new_i, new_j))

        return res









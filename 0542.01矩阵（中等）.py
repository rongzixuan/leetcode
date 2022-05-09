"""
给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。

"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:


        # 方法一：广度优先搜索
        # 时间复杂度：O(m * n)
        # 空间复杂度：：O(m * n)
        m, n = len(mat), len(mat[0])
        res_mat = [[0] * n for _ in range(m)]

        queue = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))

        while queue:
            i, j, depth = queue.pop(0)

            for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= new_i < m and 0 <= new_j < n and mat[new_i][new_j] == 1:
                    mat[new_i][new_j] = 0
                    #print(new_i, new_j)
                    res_mat[new_i][new_j] = depth + 1
                    queue.append((new_i, new_j, depth+1))

        return res_mat


        # 方法二：动态规划
        # 时间复杂度：O(m * n)
        # 空间复杂度：：O(m * n)
        m, n = len(mat), len(mat[0])
        res_mat = [[float('inf')] * n for _ in range(m)]
        #print(res_mat)

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res_mat[i][j] = 0

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    res_mat[i][j] = min(res_mat[i][j], res_mat[i-1][j] + 1)
                if j - 1 >= 0:
                    res_mat[i][j] = min(res_mat[i][j], res_mat[i][j-1] + 1)    
        
        for i in range(m-1, -1, -1):
            for j in range(n):
                if i + 1 < m:
                    res_mat[i][j] = min(res_mat[i][j], res_mat[i+1][j] + 1)
                if j - 1 >= 0:
                    res_mat[i][j] = min(res_mat[i][j], res_mat[i][j-1] + 1)

        for i in range(m):
            for j in range(n-1, -1, -1):
                if i - 1 >= 0:
                    res_mat[i][j] = min(res_mat[i][j], res_mat[i-1][j] + 1)
                if j + 1 < n:
                    res_mat[i][j] = min(res_mat[i][j], res_mat[i][j+1] + 1)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i + 1 < m:
                    res_mat[i][j] = min(res_mat[i][j], res_mat[i+1][j] + 1)
                if j + 1 < n:
                    res_mat[i][j] = min(res_mat[i][j], res_mat[i][j+1] + 1)

        return res_mat


        # 方法三：动态规划2
        # 时间复杂度：O(m * n)
        # 空间复杂度：：O(m * n)
        m, n = len(mat), len(mat[0])
        res_mat = [[float('inf')] * n for _ in range(m)]
        #print(res_mat)

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res_mat[i][j] = 0

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    res_mat[i][j] = min(res_mat[i][j], res_mat[i-1][j] + 1)
                if j - 1 >= 0:
                    res_mat[i][j] = min(res_mat[i][j], res_mat[i][j-1] + 1)    

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i + 1 < m:
                    res_mat[i][j] = min(res_mat[i][j], res_mat[i+1][j] + 1)
                if j + 1 < n:
                    res_mat[i][j] = min(res_mat[i][j], res_mat[i][j+1] + 1)

        return res_mat






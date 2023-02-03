"""
给你一个 m x n 的矩阵 matrix ，请你返回一个新的矩阵 answer ，其中 answer[row][col] 是 matrix[row][col] 的秩。

每个元素的 秩 是一个整数，表示这个元素相对于其他元素的大小关系，它按照如下规则计算：
秩是从 1 开始的一个整数。
如果两个元素 p 和 q 在 同一行 或者 同一列 ，那么：
如果 p < q ，那么 rank(p) < rank(q)
如果 p == q ，那么 rank(p) == rank(q)
如果 p > q ，那么 rank(p) > rank(q)
秩 需要越 小 越好。

题目保证按照上面规则 answer 数组是唯一的。

示例 1：
输入：matrix = [[1,2],[3,4]]
输出：[[1,2],[2,3]]
解释：
matrix[0][0] 的秩为 1 ，因为它是所在行和列的最小整数。
matrix[0][1] 的秩为 2 ，因为 matrix[0][1] > matrix[0][0] 且 matrix[0][0] 的秩为 1 。
matrix[1][0] 的秩为 2 ，因为 matrix[1][0] > matrix[0][0] 且 matrix[0][0] 的秩为 1 。
matrix[1][1] 的秩为 3 ，因为 matrix[1][1] > matrix[0][1]， matrix[1][1] > matrix[1][0] 且 matrix[0][1] 和 matrix[1][0] 的秩都为 2 。

示例 2：
输入：matrix = [[7,7],[7,7]]
输出：[[1,1],[1,1]]

示例 3：
输入：matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
输出：[[4,2,3],[1,3,4],[5,1,6],[1,3,4]]

示例 4：
输入：matrix = [[7,3,6],[1,4,5],[9,8,2]]
输出：[[5,1,4],[1,2,3],[6,3,1]]

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 500
-10^9 <= matrix[row][col] <= 10^9

"""

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            if self.size[pa] > self.size[pb]:
                self.p[pb] = pa
                self.size[pa] += self.size[pb]
            else:
                self.p[pa] = pb
                self.size[pb] += self.size[pa]

    def reset(self, x):
        self.p[x] = x
        self.size[x] = 1


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:


        # 方法一：并查集
        # 时间复杂度：
        # 空间复杂度：
        m, n = len(matrix), len(matrix[0])
        d = defaultdict(list)
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                d[v].append((i, j))
        row_max = [0] * m
        col_max = [0] * n
        ans = [[0] * n for _ in range(m)]
        uf = UnionFind(m + n)
        rank = defaultdict(int)
        for v in sorted(d):
            for i, j in d[v]:
                uf.union(i, j + m)
            for i, j in d[v]:
                rank[uf.find(i)] = max(rank[uf.find(i)], row_max[i], col_max[j])
            for i, j in d[v]:
                ans[i][j] = row_max[i] = col_max[j] = 1 + rank[uf.find(i)]
            for i, j in d[v]:
                uf.reset(i)
                uf.reset(j + m)
        return ans




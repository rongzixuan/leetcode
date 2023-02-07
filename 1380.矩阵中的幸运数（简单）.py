"""
给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。

幸运数是指矩阵中满足同时下列两个条件的元素：
在同一行的所有元素中最小
在同一列的所有元素中最大

示例 1：
输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
输出：[15]
解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

示例 2：
输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
输出：[12]
解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

示例 3：
输入：matrix = [[7,8],[1,2]]
输出：[7]
 
提示：
m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5
矩阵中的所有元素都是不同的

"""


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:


        # 方法一：模拟
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(1)
        res = []
        for row in matrix:
            #print(row)
            for j, x in enumerate(row):
                if x == min(row) == max(r[j] for r in matrix):
                    res.append(x)
        return res


        # 方法二：模拟2
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m + n)
        res = []
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]
        print(*matrix)
        print(zip(*matrix))
        for i, row in enumerate(matrix):
            #print(row)
            for j, x in enumerate(row):
                if x == row_min[i] == col_max[j]:
                    res.append(x)
        return res




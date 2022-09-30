"""
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

示例 1：
输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

示例 2：
输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        # 方法一：数组
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m + n)
        m, n = len(matrix), len(matrix[0])
        rows, cols = [False] * m, [False] * n
        for i, j in product(range(m), range(n)):
            #print(i, j)
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True

        for i, j in product(range(m), range(n)):
            if rows[i] == True or cols[j] == True:
                matrix[i][j] = 0


        # 方法二：数组原地标记
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(1)
        m, n = len(matrix), len(matrix[0])

        flag_row = any([matrix[0][j] == 0 for j in range(n)])
        flag_col = any([matrix[i][0] == 0 for i in range(m)])

        for i, j in product(range(1, m), range(1, n)):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

        for i, j in product(range(1, m), range(1, n)):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

        if flag_row:
            for j in range(n):
                matrix[0][j] = 0

        if flag_col:
            for i in range(m):
                matrix[i][0] = 0


        # 方法三：数组原地标记
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(1)
        m, n = len(matrix), len(matrix[0])
        flag_col = any([matrix[i][0] == 0 for i in range(m)])
        matrix[0][0] = 0 if any([matrix[0][j] == 0 for j in range(n)]) else matrix[0][0]

        for i, j in product(range(1, m), range(1, n)):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

        for i, j in product(range(1, m), range(1, n)):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(1, n):
                matrix[0][j] = 0

        if flag_col:
            for i in range(m):
                matrix[i][0] = 0




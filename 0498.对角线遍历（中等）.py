"""
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

示例 1：
输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]

示例 2：
输入：mat = [[1,2],[3,4]]
输出：[1,2,3,4]
 
提示：
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
-10^5 <= mat[i][j] <= 10^5

"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        # 方法一：模拟
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(1)
        m, n = len(mat), len(mat[0])
        flag = 1  # 定义方向
        i, j = 0, 0
        ans = []
        total = 0

        while 0 <= i < m and 0 <= j < n and total <= (m + n - 2):
            if flag == 1:
                while 0 <= i < m and 0 <= j < n and total <= (m + n - 2):
                    ans.append(mat[i][j])
                    i -= 1
                    j += 1
                if j == n:
                    i, j = i + 2, n - 1
                else:
                    i, j = 0, j               
            elif flag == -1:
                while 0 <= i < m and 0 <= j < n and total <= (m + n - 2):
                    ans.append(mat[i][j])
                    i += 1
                    j -= 1
                if i == m:
                    i, j = i - 1, j + 2
                else:
                    i, j = i, 0                
            flag = -flag
            total += 1

        return ans



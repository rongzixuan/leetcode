"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # 方法一：二分查找
        # 时间复杂度：O(m * logn)
        # 空间复杂度：O(1)
        m, n = len(matrix), len(matrix[0])
        #print(m, n)

        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                #print('i:', i)
                left, right = 0, n-1
                while left <= right:
                    #print(left, right)
                    mid = left + (right - left) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

        #print(left, right)
        return False


        # 方法二：z字形查找
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(1)
        m, n = len(matrix), len(matrix[0])

        i, j = 0, n-1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1

        return False

        






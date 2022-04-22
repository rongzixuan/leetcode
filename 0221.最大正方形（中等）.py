"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m, n = len(matrix), len(matrix[0])

        # 方法一：动态规划
        dp = [[0] * (n+1) for _ in range(m+1)]

        max_length = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    max_length = max(max_length, dp[i][j])

        return max_length * max_length


        # 方法二：位运算
        def getWith(num):
            count = 0
            while num:
                count += 1
                num = (num << 1) & num
            return count

        #pre_num = 0
        
        nums = [0] * m # 存放二进制数
        for i in range(m):
            num = 0
            for j in range(0, n):
                num = num * 2 + int(matrix[i][j])
            nums[i] = num
        #print('nums:', nums)

        # 枚举最大长度
        max_length = 0     
        for i in range(m):
            num = nums[i]
            for j in range(i, m):
                num &= nums[j]
                width = getWith(num)
                #print('num:', num)
                #print('width:', width)
                max_length = max(max_length, min(j-i+1, width))

        return max_length * max_length
    
    
    
    

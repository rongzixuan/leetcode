"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        dp = [[0] * (i+1) for i in range(n)]
        dp[0][0] = triangle[0][0]
        print(dp)

        for i in range(1, n):
            for j in range(i+1):
                if j == 0:
                    dp[i][0] = dp[i-1][0] + triangle[i][0]
                elif j == i:
                    dp[i][i] = dp[i-1][i-1] + triangle[i][i]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

        return min(dp[n-1])


        # 方法二：动态规划2
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        dp = [[0] * n for i in range(2)]
        dp[0][0] = triangle[0][0]
        #print(dp)

        for i in range(1, n):                
            if i % 2 == 1:
                pre, aft = 0, 1
            else:
                pre, aft = 1, 0

            for j in range(i+1):
                if j == 0:
                    dp[aft][0] = dp[pre][0] + triangle[i][0]
                elif j == i:
                    dp[aft][i] = dp[pre][i-1] + triangle[i][i]
                else:
                    dp[aft][j] = min(dp[pre][j-1], dp[pre][j]) + triangle[i][j]

        #print(dp)
        return min(dp[1]) if n % 2 == 0 else min(dp[0])


        # 方法三：动态规划3
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        dp = [0] * n
        dp[0] = triangle[0][0]
        #print(dp)

        for i in range(1, n):                
            for j in range(i, -1, -1):  # 注意是从后往前的顺序
                if j == i:
                    dp[i] = dp[i-1] + triangle[i][i]
                elif 0 < j < i:
                    dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
                elif j == 0:
                    dp[0] = dp[0] + triangle[i][0]
            #print(dp)

        #print(dp)
        return min(dp) 

        






"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
"""

class Solution:
    def climbStairs(self, n: int) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if n == 1 or n == 2:
            return n

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]


        # 方法二：动态规划2
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        if n == 1 or n == 2:
            return n
            
        a, b = 1, 2

        for i in range(2, n):
            c = a + b
            a = b
            b = c

        return c
    
    
    
    

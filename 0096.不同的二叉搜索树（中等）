"""
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

"""

class Solution:
    def numTrees(self, n: int) -> int:

        # 方法一：动态规划
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1): # 根节点
                dp[i] += dp[j-1] * dp[i-j]
        #print(dp)
        return dp[n]
        
        
        # 方法二：数学（卡塔兰数）
        res = 1

        for i in range(0, n):
            res = res * 2 * (2*i+1) / (i+2)

        return int(res)

"""
给出两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个逆序对的不同的数组的个数。
逆序对的定义如下：对于数组的第i个和第 j个元素，如果满i < j且 a[i] > a[j]，则其为一个逆序对；否则不是。
由于答案可能很大，只需要返回 答案 mod 109 + 7 的值。

示例 1:
输入: n = 3, k = 0
输出: 1
解释: 
只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。

示例 2:
输入: n = 3, k = 1
输出: 2
解释: 
数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。
说明:

 n 的范围是 [1, 1000] 并且 k 的范围是 [0, 1000]。

"""

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        # 方法一：动态规划
        # 时间复杂度：
        # 空间复杂度：O(n * k)
        if k == 0:
            return 1

        dp = [[0] * (k+1) for _ in range(n+1)]  # dp[i][j]表示使用数字1-i，有j个逆序对的数量
        for i in range(n+1):
            dp[i][0] = 1
            #if i > 1:
            #    dp[i][1] = i-1
        #print(dp)

        res = 0
        # f[i][j] = f[i][j−1] − f[i−1][j−i] + f[i−1][j]
        for i in range(1, n+1):
            for j in range(k+1):
                if j == 0 and j < i:
                    dp[i][j] = dp[i-1][j] + 0 - 0
                #elif j == 0:
                #    dp[i][j] = dp[i-1][j] + 0 - dp[i-1][j-i]
                elif j < i:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] - 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-i]
        #print(dp[99][:])

        MOD = 10**9+7
        return dp[n][k] % MOD



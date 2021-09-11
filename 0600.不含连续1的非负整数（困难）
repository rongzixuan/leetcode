"""
给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。

"""


class Solution:
    def findIntegers(self, n: int) -> int:

        # 方法一：动态规划
        # 时间复杂度：O(logn)
        # 空间复杂度：O(logn)
        if n < 3:
            return n + 1

        count = 0    
        dp = [0] * 31
        dp[0] = dp[1] = 1
        for i in range(2, 31):
            dp[i] = dp[i-1] + dp[i-2]

        res = 0
        pre = 0
        for i in range(29, -1, -1):
            val = 1 << i
            if n & val:
                res += dp[i+1]
                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0

            if i == 0:
                res += 1

        return res




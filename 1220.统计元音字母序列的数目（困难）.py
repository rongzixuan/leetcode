"""
给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：

字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
每个元音 'a' 后面都只能跟着 'e'
每个元音 'e' 后面只能跟着 'a' 或者是 'i'
每个元音 'i' 后面 不能 再跟着另一个 'i'
每个元音 'o' 后面只能跟着 'i' 或者是 'u'
每个元音 'u' 后面只能跟着 'a'

由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。

示例 1：
输入：n = 1
输出：5
解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。

示例 2：
输入：n = 2
输出：10
解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。

示例 3：
输入：n = 5
输出：68

提示：
1 <= n <= 2 * 10^4

"""


class Solution:
    def countVowelPermutation(self, n: int) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(c * n)
        # 空间复杂度：O(c * n)
        # c = 5
        MOD = 10 ** 9 + 7
        dp = [[0] * 5 for i in range(n + 1)]
        dp[1] = [1, 1, 1, 1, 1]
        #print(dp)

        for i in range(2, n + 1):
            dp[i] = [dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4],
                     dp[i - 1][0] + dp[i - 1][2],
                     dp[i - 1][1] + dp[i - 1][3], 
                     dp[i - 1][2],
                     dp[i - 1][2] + dp[i - 1][3]]
        #print(dp)

        return sum(dp[-1]) % MOD


        # 方法二：快速矩阵幂
        # 时间复杂度：O(c^3 * n)
        # 空间复杂度：O(c^2)
        # c = 5
        import numpy as np
        MOD = 10 ** 9 + 7
        factor = np.mat([(0, 1, 0, 0, 0), 
                  (1, 0, 1, 0, 0), 
                  (1, 1, 0, 1, 1), 
                  (0, 0, 1, 0, 1), 
                  (1, 0, 0, 0, 0)], np.dtype('O'))

        res = np.mat([(1, 1, 1, 1, 1)], np.dtype('O'))

        n -= 1
        while n > 0:
            if n % 2 == 1:
                res *= factor 
            factor = factor * factor
            n //= 2

        #print(res)
        return res.sum() % MOD
                



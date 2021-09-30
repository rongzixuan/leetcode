"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(m*n)
        # 空间复杂度：O(m*n)
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return m + n

        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i

        for j in range(1, n+1):
            dp[0][j] = j

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1

        #print(dp)
        return dp[m][n]





"""
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        # 方法一：最长公共子序列（动态规划）
        # 时间复杂度：O(n1 * n2)
        # 空间复杂度：O(n1 * n2)
        n1, n2 = len(word1), len(word2)
        sub_n = 0
        dp = [[0] * (n2+1) for _ in range(n1+1)]

        for i in range(n1):
            for j in range(n2):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        #print(dp)
        sub_n = dp[n1][n2]
        return n1 + n2 - 2 * sub_n



        # 方法二：动态规划
        # 时间复杂度：O(n1 * n2)
        # 空间复杂度：O(n1 * n2)
        n1, n2 = len(word1), len(word2)       
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)] # dp[i][j]为需要删除的字符个数

        for i in range(n1):
            dp[i+1][0] = i+1
        for i in range(n2):
            dp[0][i+1] = i+1

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

        #print(dp)
        return dp[n1][n2]





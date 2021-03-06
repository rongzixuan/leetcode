"""
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(s)
        if n == 1:
            return 1

        #max_length = 1
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                        #max_length = max(max_length, dp[i][j])
                    else:
                        dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        #print(dp)
        return dp[0][n-1]



        # 方法二：动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(s)
        if n == 1:
            return 1
        s_ = s[::-1]   # 翻转字符串
        dp = [[0] * (n+1) for _ in range(n+1)]

        #寻找s和s_的最长公共子序列
        for i in range(0, n):
            for j in range(n):
                if s[i] == s_[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[n][n]






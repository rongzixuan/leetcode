"""
可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
'A'：Absent，缺勤
'L'：Late，迟到
'P'：Present，到场

如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
按 总出勤 计，学生缺勤（'A'）严格 少于两天。
学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。

给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。答案可能很大，所以返回对 109 + 7 取余 的结果。

"""

class Solution:
    def checkRecord(self, n: int) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)

        # dp[i][0]为满足条件1的个数
        # dp[i][1]为满足条件2的个数
        MOD = 10 ** 9 + 7
        dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(n+1)]
        dp[0][0][0] = 1
        #print(dp)

        # i为长度，j为'A'的个数，k为连续'L'的个数
        for i in range(1, n+1):
            # 以'P'结尾
            for j in range(2):
                for k in range(3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD

            # 以'A'结尾
            for k in range(3):
                dp[i][1][0] = (dp[i][1][0] + dp[i-1][0][k]) % MOD

            # 以'L'结尾：
            for j in range(2):
                for k in range(2):
                    dp[i][j][k+1] = (dp[i][j][k+1] + dp[i-1][j][k]) % MOD

        #print(dp)
        res = 0
        for j in range(2):
            for k in range(3):
                res += dp[n][j][k]

        return res % MOD




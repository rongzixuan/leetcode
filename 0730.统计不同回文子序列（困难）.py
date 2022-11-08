"""
给定一个字符串 s，返回 s 中不同的非空「回文子序列」个数 。

通过从 s 中删除 0 个或多个字符来获得子序列。
如果一个字符序列与它反转后的字符序列一致，那么它是「回文字符序列」。

如果有某个 i , 满足 ai != bi ，则两个序列 a1, a2, ... 和 b1, b2, ... 不同。

注意：
结果可能很大，你需要对 109 + 7 取模 。

示例 1：
输入：s = 'bccb'
输出：6
解释：6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
注意：'bcb' 虽然出现两次但仅计数一次。

示例 2：
输入：s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
输出：104860361
解释：共有 3104860382 个不同的非空回文子序列，104860361 对 109 + 7 取模后的值。
 
提示：
1 <= s.length <= 1000
s[i] 仅包含 'a', 'b', 'c' 或 'd'

"""

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:


        # 方法一：动态规划 + 哈希表
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        mod = 1000000007
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n): dp[i][i] = 1

        for cur_len in range(2, n+1):  # 从长度为2的子串开始计算
            # 挨个计算长度为len的子串的回文子序列个数
            for i in range(0, n-cur_len+1):
                j = i+ cur_len -1
                # 情况(1) 相等
                if s[i] == s[j]:
                    l, r = i+1, j-1
                    while l <= r and s[l] != s[i]: l += 1
                    while l <= r and s[r] != s[j]: r -= 1
                    if l > r:  # 情况① 没有重复字符
                        dp[i][j] = 2 * dp[i+1][j-1] + 2
                    elif l == r:   # 情况② 出现一个重复字符
                        dp[i][j] = 2 * dp[i+1][j-1] + 1
                    else:  # 情况③ 有两个及两个以上
                        dp[i][j] = 2 * dp[i+1][j-1] - dp[l+1][r-1]
                else:  # 情况(2) 不相等
                    dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1]
                dp[i][j] = dp[i][j] % mod  # Python直接取模也没有问题
        return dp[0][n-1]



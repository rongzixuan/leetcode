"""
给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，那么单词 word 的 重复值为 k 。单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。如果 word 不是 sequence 的子串，那么重复值 k 为 0 。
给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。

示例 1：
输入：sequence = "ababc", word = "ab"
输出：2
解释："abab" 是 "ababc" 的子字符串。

示例 2：
输入：sequence = "ababc", word = "ba"
输出：1
解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。

示例 3：
输入：sequence = "ababc", word = "ac"
输出：0
解释："ac" 不是 "ababc" 的子字符串。
 
提示：
1 <= sequence.length <= 100
1 <= word.length <= 100
sequence 和 word 都只包含小写英文字母。

"""

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n * m)
        # 空间复杂度：O(n)
        n, m = len(sequence), len(word)
        ans = 0
        i = 0
        dp = [0] * (n + 1)
        while i < n:
            if i + 1 - m >= 0 and sequence[i - m + 1: i + 1]== word:
                dp[i + 1] = dp[i + 1 - m] + 1
            i += 1
        return max(dp)


        # 方法二：KMP算法
        # 时间复杂度：O(n + m)
        # 空间复杂度：O(n + m)
        n, m = len(sequence), len(word)
        if n < m:
            return 0

        fail = [-1] * m
        for i in range(1, m):
            j = fail[i - 1]
            while j != -1 and word[j + 1] != word[i]:
                j = fail[j]
            if word[j + 1] == word[i]:
                fail[i] = j + 1
        
        f = [0] * n
        j = -1
        for i in range(n):
            while j != -1 and word[j + 1] != sequence[i]:
                j = fail[j]
            if word[j + 1] == sequence[i]:
                j += 1
                if j == m - 1:
                    f[i] = (0 if i == m - 1 else f[i - m]) + 1
                    j = fail[j]
        
        return max(f)





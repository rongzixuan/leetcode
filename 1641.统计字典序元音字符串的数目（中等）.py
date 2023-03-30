"""
给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。

字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。

示例 1：
输入：n = 1
输出：5
解释：仅由元音组成的 5 个字典序字符串为 ["a","e","i","o","u"]

示例 2：
输入：n = 2
输出：15
解释：仅由元音组成的 15 个字典序字符串为
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后

示例 3：
输入：n = 33
输出：66045
 
提示：
1 <= n <= 50

"""

class Solution:
    def countVowelStrings(self, n: int) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n * C^2)
        # 空间复杂度：O(n * C)
        # C = 5
        dp = [[0] * 5 for _ in range(n + 1)]
        for i in range(5):
            dp[1][i] = 1

        for i in range(2, n + 1):
            for j in range(5):
                for k in range(j + 1):
                    dp[i][j] += dp[i - 1][k]
        #print(dp)
        return sum([dp[n][i] for i in range(5)])


        # 方法二：动态规划
        # 时间复杂度：O(n * C)
        # 空间复杂度：O(n * C)
        # C = 5
        dp = [1] * 5
        for _ in range(n - 1):
            for j in range(1, 5):
                dp[j] += dp[j - 1]
        return sum(dp)


        # 方法三：记忆化搜索
        # 时间复杂度：O(n * C^2)
        # 空间复杂度：O(n * C)
        # C = 5
        @cache
        def dfs(i, j):
            if i == 1:
                return 1
            else:
                return sum([dfs(i - 1, k) for k in range(j + 1)])

        return sum([dfs(n, k) for k in range(5)])





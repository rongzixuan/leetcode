"""
给你一个字符串 s ，它仅包含字符 'a' 和 'b'。

你可以删除 s 中任意数目的字符，使得 s 平衡 。当不存在下标对 (i,j) 满足 i < j ，且 s[i] = 'b' 的同时 s[j]= 'a' ，此时认为 s 是 平衡 的。

请你返回使 s 平衡 的 最少 删除次数。

示例 1：
输入：s = "aababbab"
输出：2
解释：你可以选择以下任意一种方案：
下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。

示例 2：
输入：s = "bbaaaaabb"
输出：2
解释：唯一的最优解是删除最前面两个字符。
 
提示：
1 <= s.length <= 10^5
s[i] 要么是 'a' 要么是 'b'​ 。​

"""

class Solution:
    def minimumDeletions(self, s: str) -> int:


        # 方法一：前缀和
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(s)
        count_left, count_right = [0] * n, [0] * n
        count1, count2 = 0, 0
        for i in range(n):
            if s[i] == 'b':
                count1 += 1
            if s[n - 1 - i] == 'a':
                count2 += 1
            count_left[i] = count1
            count_right[n - 1 - i] = count2
        #print(count_left)
        #print(count_right)

        ans = inf
        for i in range(n):
            ans = min(ans, count_left[i] + count_right[i] - 1)
        return ans


        # 方法二：动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(s)
        f = [0] * (n + 1)
        b = 0
        for i, c in enumerate(s, 1):
            if c == 'b':
                f[i] = f[i - 1]
                b += 1
            else:
                f[i] = min(f[i - 1] + 1, b)
        return f[n]






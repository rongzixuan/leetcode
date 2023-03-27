"""
给你两个字符串 s 和 t ，请你找出 s 中的非空子串的数目，这些子串满足替换 一个不同字符 以后，是 t 串的子串。换言之，请你找到 s 和 t 串中 恰好 只有一个字符不同的子字符串对的数目。

比方说， "computer" and "computation" 只有一个字符不同： 'e'/'a' ，所以这一对子字符串会给答案加 1 。

请你返回满足上述条件的不同子字符串对数目。

一个 子字符串 是一个字符串中连续的字符。

示例 1：
输入：s = "aba", t = "baba"
输出：6
解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
加粗部分分别表示 s 和 t 串选出来的子字符串。

示例 2：
输入：s = "ab", t = "bb"
输出：3
解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
("ab", "bb")
("ab", "bb")
("ab", "bb")
加粗部分分别表示 s 和 t 串选出来的子字符串。

示例 3：
输入：s = "a", t = "a"
输出：0

示例 4：
输入：s = "abe", t = "bbc"
输出：10

提示：
1 <= s.length, t.length <= 100
s 和 t 都只包含小写英文字母。

"""

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:


        # 方法一：枚举
        # 时间复杂度：O(m * n * min(m, n) * min(m, n))
        # 空间复杂度：O()
        n, m = len(s), len(t)
        length = min(m, n)
        ans = 0
        
        for i in range(0, n):        
            for j in range(0, m):                                   
                for l in range(1, length + 1):
                    if i + l <= n and j + l <= m:
                        a = s[i: i + l]
                        b = t[j: j + l]
                        #print('a, b:', a, b)
                        count = 0
                        for k in range(len(a)):
                            if a[k] != b[k]:
                                count += 1
                            if count >= 2:
                                break
                        if count == 1:
                            ans += 1
        return ans


        # 方法二：枚举
        # 时间复杂度：O(m * n * min(m, n))
        # 空间复杂度：O(1)
        """我们可以枚举字符串 s 和 t 中不同的那个字符位置，然后分别向两边扩展，直到遇到不同的字符为止，这样就可以得到以该位置为中心的满足条件的子串对数目。我们记左边扩展的相同字符个数为 l，右边扩展的相同字符个数为 r，那么以该位置为中心的满足条件的子串对数目为 (l+1)×(r+1)，累加到答案中即可。"""
        ans = 0
        m, n = len(s), len(t)
        for i, a in enumerate(s):
            for j, b in enumerate(t):
                if a != b:
                    l = r = 0
                    while i > l and j > l and s[i - l - 1] == t[j - l - 1]:
                        l += 1
                    while i + r + 1 < m and j + r + 1 < n and s[i + r + 1] == t[j + r + 1]:
                        r += 1
                    ans += (l + 1) * (r + 1)
        return ans


        # 方法三：枚举
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        ans = 0
        m, n = len(s), len(t)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        g = [[0] * (n + 1) for _ in range(m + 1)]
        for i, a in enumerate(s, 1):
            for j, b in enumerate(t, 1):
                if a == b:
                    f[i][j] = f[i - 1][j - 1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    g[i][j] = g[i + 1][j + 1] + 1
                else:
                    ans += (f[i][j] + 1) * (g[i + 1][j + 1] + 1)
        return ans






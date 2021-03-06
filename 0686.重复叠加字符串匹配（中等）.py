"""
给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。
注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。

示例 1：
输入：a = "abcd", b = "cdabcdab"
输出：3
解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。

示例 2：
输入：a = "a", b = "aa"
输出：2

示例 3：
输入：a = "a", b = "a"
输出：1

示例 4：
输入：a = "abc", b = "wxyz"
输出：-1

提示：
1 <= a.length <= 10^4
1 <= b.length <= 10^4
a 和 b 由小写英文字母组成

"""

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:


        # 方法一：暴力法
        # 时间复杂度：O((m+n) * (m+n))
        # 空间复杂度：O(1)
        m, n = len(a), len(b)
        max_length = 2 * m + n
        tmp_length = m
        tmp_a = a

        res = 1
        while tmp_length <= max_length:
            if b in tmp_a:
                return res
            else:
                tmp_a += a
                tmp_length += m
                res += 1

        return -1


        # 方法二：Rabin-Karp算法
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(1)
        def strstr(a, b):
            m, n = len(a), len(b)
            if n == 0:
                return 0
            
            k1, k2 = 10 ** 9 + 7, 1337
            mod1, mod2 = randrange(k1) + k1, randrange(k2) + k2

            hash_b = 0
            for i in range(n):
                hash_b = (hash_b * mod2 + ord(b[i])) % mod1

            hash_a = 0
            for i in range(n-1):
                hash_a = (hash_a * mod2 + ord(a[i % m])) % mod1

            extra = pow(mod2, n - 1, mod1)
            for i in range(n - 1, m + n - 1):
                hash_a = (hash_a * mod2 + ord(a[i % m])) % mod1
                if hash_a == hash_b:
                    return i - n + 1
                hash_a = (hash_a - extra * ord(a[(i - n + 1) % m])) % mod1
                hash_a = (hash_a + mod1) % mod1
            return -1

        m, n = len(a), len(b)
        index = strstr(a, b)
        if index == -1:
            return -1
        elif index <= m - n:
            return 1
        else:
            return (n + index - m - 1) // m + 2


        # 方法三：Knuth-Morris-Pratt 算法
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(n)
        def strstr(a, b):
            m, n = len(a), len(b)
            if n == 0:
                return 0

            next_ = [0] * n
            left = 0
            for right in range(1, n):
                #print('left, right:', left, right)
                while left > 0 and b[left] != b[right]:
                    left = next_[left - 1]
                if b[left] == b[right]:
                    left += 1
                next_[right] = left

            i, j = 0, 0
            while i - j < m:
                #print('i, j:', i, j)
                while j > 0 and a[i % m] != b[j]:
                    j = next_[j - 1] 
                if a[i % m] == b[j]:                    
                    j += 1
                if j == n:
                    return i - n + 1
                i += 1
            return -1

        m, n = len(a), len(b)
        index = strstr(a, b)
        if index == -1:
            return -1
        elif index <= m - n:
            return 1
        else:
            return (n + index - m - 1) // m + 2




"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

"""

class Solution:
    def reverseWords(self, s: str) -> str:


        # 方法一：遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(s)
        if n == 1:
            return s

        res = ""
        i = j = 0
        while i < n:
            while i < n and s[i] != " ":
                i += 1
            for k in range(i-1, j-1, -1):
                res += s[k]
            res += " "
            i += 1
            j = i

        return res.strip()


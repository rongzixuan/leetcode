"""
给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。
 
示例 1：
输入：s = "Hello"
输出："hello"

示例 2：
输入：s = "here"
输出："here"

示例 3：
输入：s = "LOVELY"
输出："lovely"
 
提示：
1 <= s.length <= 100
s 由 ASCII 字符集中的可打印字符组成

"""

class Solution:
    def toLowerCase(self, s: str) -> str:

        # 方法一：模拟
        # 时间复杂度：
        # 空间复杂度：
        return s.lower()


        # 方法二：模拟2
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        res = ""
        for ch in s:
            if 65 <= ord(ch) <= 90:
                res += chr(ord(ch) | 32)
            else:
                res += ch

        return res


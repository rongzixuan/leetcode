"""
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:


        # 方法一：字符串模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        s = s.strip(' ') # 移除字符串头尾指定的字符
        #print(s.split(" "))
        return len(s.split(' ')[-1])


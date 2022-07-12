"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

"""


class Solution:
    def countSegments(self, s: str) -> int:

        # 方法一：
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(s)
        res = 0

        for i in range(n):
            if i == n-1 and s[i] != ' ':
                #print('1:', i)
                res += 1
            elif i != 0 and s[i] == ' ' and s[i-1] != ' ':
                #print('2:', i)
                res += 1

        return res

    
    
    

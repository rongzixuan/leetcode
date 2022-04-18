"""
给定一个Excel表格中的列名称，返回其相应的列序号。

"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        # 方法一：进制转换
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)

        n = len(columnTitle)
        res = 0

        for i in range(n):
            num = ord(columnTitle[i]) - ord('A') + 1
            res = res * 26 + num

        #print(res)
        return res



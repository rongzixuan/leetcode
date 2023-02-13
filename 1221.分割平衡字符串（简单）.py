"""
在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。

给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

注意：分割得到的每个字符串都必须是平衡字符串。

返回可以通过分割得到的平衡字符串的 最大数量 。

"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:


        # 方法一：计数
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        count = 0
        res = 0
        n = len(s)
        if n == 2:
            return 1

        for i in range(n):
            if s[i] == 'L':
                count += 1
            elif s[i] == 'R':
                count -= 1
            
            if count == 0:
                res += 1

        return res


    
    

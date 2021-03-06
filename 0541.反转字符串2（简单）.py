"""
给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:


        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(s)
        a = list(s)
        #print(a)

        for i in range(0, n, 2*k):
            #print(i, i+k) 
            a[i: i+k] = reversed(a[i: i+k])

        #print(a)
        return ''.join(a)


        # 方法二：模拟2
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(s)
        a = list(s)
        #print(a)

        for i in range(0, n, 2*k):
            #print(i, i+k) 
            a[i: i+k] = reversed(a[i: min(i+k, n)])

        #print(a)
        return ''.join(a)

    
    

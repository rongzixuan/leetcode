"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """


        # 方法一：双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(s)
        if n == 1:
            return n

        i, j = 0, n-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1






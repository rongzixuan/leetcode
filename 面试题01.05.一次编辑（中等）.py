"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

示例 1:
输入: 
first = "pale"
second = "ple"
输出: True
 
示例 2:
输入: 
first = "pales"
second = "pal"
输出: False

"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:


        # 方法一：模拟
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(1)
        if first == second:
            return True
        m, n = len(first), len(second)
        if abs(m - n) > 1:
            return False
        if m < n:
            first, second = second, first
        if n == 0:
            return True

        if m == n:  # 替换
            count = sum([1 if ch1 != ch2 else 0 for ch1, ch2 in zip(first, second)])
            return True if count < 2 else False
        else:       # 删除         
            i, j = 0, 0
            count = 0
            while i < m and j < n:
                if first[i] != second[j]:
                    i += 1
                    count += 1
                else:
                    i += 1
                    j += 1
                if count > 1:
                    return False
            return True


        # 方法二：模拟
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(1)
        m, n = len(first), len(second)
        if m < n:
            return self.oneEditAway(second, first)
        if m - n > 1:
            return False
        for i, (x, y) in enumerate(zip(first, second)):
            if x != y:
                return first[i + 1:] == second[i + 1:] if m == n else first[i + 1:] == second[i:]  # 注：改用下标枚举可达到 O(1) 空间复杂度
        return True






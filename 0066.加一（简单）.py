"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:


        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(digits)
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        digits[-1] = 0
        for i in range(n-2, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        digits.insert(0, 1)
        return digits


    
    

"""
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法

"""


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """

        # 方法一：拒绝采样
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)

        while True: # 直到生成的数字满足要求，有返回值
            a = rand7()
            b = rand7()

            idx = (a-1) * 7 + b
            if idx <= 40:
                return idx % 10 + 1


        # 方法2：拒绝采样进阶
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        while True:
            a, b = rand7(), rand7()
            idx = (a - 1) * 7 + b
            if idx <= 40:
                return idx % 10 + 1
            else:
                a = idx - 40
                b = rand7()
                idx = (a-1) * 7 + b
                if idx <= 60:
                    return idx % 10 + 1
                else:
                    a = idx - 60
                    b = rand7()
                    idx = (a - 1) * 7 + b
                    if idx <= 20:
                        return idx % 10 + 1


                    
                    

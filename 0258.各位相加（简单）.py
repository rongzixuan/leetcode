"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

 

示例 1:
输入: num = 38
输出: 2 
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于 2 是一位数，所以返回 2。

示例 2:
输入: num = 0
输出: 0
 

提示：
0 <= num <= 2^31 - 1

进阶：你可以不使用循环或者递归，在 O(1) 时间复杂度内解决这个问题吗？

"""


class Solution:
    def addDigits(self, num: int) -> int:


        # 方法一：模拟
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        #print(str(num))
        #print(list(str(num)))
        #print(sum([int(x) for x in list(str(num))]))
        while num > 9:
            tmp_sum = sum([int(x) for x in list(str(num))])
            num = tmp_sum

        return num


        # 方法二：数学
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        return (num - 1) % 9 + 1 if num else 0




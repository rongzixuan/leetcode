"""
累加数 是一个字符串，组成它的数字可以形成累加序列。

一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。

说明：累加序列里的数 不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
 

示例 1：
输入："112358"
输出：true 
解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

示例 2：
输入："199100199"
输出：true 
解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
 

提示：
1 <= num.length <= 35
num 仅由数字（0 - 9）组成
 
进阶：你计划如何处理由过大的整数输入导致的溢出?

"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:


        # 方法一：枚举
        # 时间复杂度：O(n^3)
        # 空间复杂度：O(n)
        n = len(num)
        if n < 3:
            return False

        def check(num1, num2, index):
            while index < n:
                tmp_sum = str(int(num1) + int(num2))
                #print('tmp_sum:', tmp_sum)
                #print(num[index: index + len(tmp_sum)])
                if num[index: index + len(tmp_sum)] != tmp_sum:
                    return False
                else:
                    index += len(tmp_sum)
                    num1, num2 = num2, int(tmp_sum)
            return True

        for i in range(n - 2):
            if num[0] == '0' and i > 0:
                continue
            for j in range(i + 1, n - 1):
                if num[i + 1] == '0' and j - i > 1:
                    continue
                num1 = num[: i+1]
                num2 = num[i+1: j+1]
                #print('num1, num2:', num1, num2)
                if check(num1, num2, j + 1):
                    return True

        return False









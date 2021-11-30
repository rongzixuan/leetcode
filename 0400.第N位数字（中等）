"""
给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位数字。


示例 1：
输入：n = 3
输出：3

示例 2：
输入：n = 11
输出：0
解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
 

提示：
1 <= n <= 2^31 - 1

"""

class Solution:
    def findNthDigit(self, n: int) -> int:


        # 方法一：模拟
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        total = 0       # 数字序列总长度
        num = 0         # 最大数字
        i = 1           # 10的指数
        while total < n:
            total += i * 9 * 10**(i-1)
            num = num * 10 + 9 
            i += 1 
            #print('total, num:', total, num)
        #print('i, totaln num:', i, total, num)

        i -= 1
        count = (total - n) // i + 1  # total和n间隔了几个数字
        #print('count:', count)
        pre_total = total - count * i            # 第n个数字之前的数字序列长度
        #print('pre_total:', pre_total)

        pre_num = num - count      # 第n个数字之前的数字
        #print('pre_num:', pre_num)

        return int(str(pre_num + 1)[n - pre_total - 1])




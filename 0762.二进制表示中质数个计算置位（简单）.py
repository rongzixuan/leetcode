"""
给你两个整数 left 和 right ，在闭区间 [left, right] 范围内，统计并返回 计算置位位数为质数 的整数个数。

计算置位位数 就是二进制表示中 1 的个数。

例如， 21 的二进制表示 10101 有 3 个计算置位。
 
示例 1：
输入：left = 6, right = 10
输出：4
解释：
6 -> 110 (2 个计算置位，2 是质数)
7 -> 111 (3 个计算置位，3 是质数)
9 -> 1001 (2 个计算置位，2 是质数)
10-> 1010 (2 个计算置位，2 是质数)
共计 4 个计算置位为质数的数字。

示例 2：
输入：left = 10, right = 15
输出：5
解释：
10 -> 1010 (2 个计算置位, 2 是质数)
11 -> 1011 (3 个计算置位, 3 是质数)
12 -> 1100 (2 个计算置位, 2 是质数)
13 -> 1101 (3 个计算置位, 3 是质数)
14 -> 1110 (3 个计算置位, 3 是质数)
15 -> 1111 (4 个计算置位, 4 不是质数)
共计 5 个计算置位为质数的数字。
 
提示：
1 <= left <= right <= 10^6
0 <= right - left <= 10^4

"""


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:


        # 方法一：位运算
        # 时间复杂度：o(nlogn)
        # 空间复杂度：O(1)
        ans = 0

        for num in range(left, right + 1):
            tmp = num
            count = 0
            while tmp:
                count += (tmp & 1)
                tmp >>= 1

            flag = True
            if count < 2:
                flag = False
            for i in range(2, int(count ** 0.5) + 1):
                if count % i == 0:
                    flag = False
                    break
            if flag:
                ans += 1

        return ans


        # 方法二：位运算
        # 时间复杂度：o(n)
        # 空间复杂度：O(1)
        ans = 0
        for num in range(left, right + 1):
            #print(num.bit_count())
            #print(1 << num.bit_count())
            if (1 << num.bit_count()) & 665772 != 0:
                ans += 1

        return ans





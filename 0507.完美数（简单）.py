"""
对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。

给定一个 整数 n， 如果是完美数，返回 true，否则返回 false


示例 1：
输入：num = 28
输出：true
解释：28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, 和 14 是 28 的所有正因子。

示例 2：
输入：num = 6
输出：true

示例 3：
输入：num = 496
输出：true

示例 4：
输入：num = 8128
输出：true

示例 5：
输入：num = 2
输出：false
 

提示：
1 <= num <= 10^8

"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:


        # 方法一：模拟（超时）
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        if num <= 0:
            return False

        total = 1
        start = int(sqrt(num))
        print(start)

        for i in range(2, num):
            if num % i == 0# 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        if num <= 0:
            return False

        total = 1
        start = int(sqrt(num))
        print(start)

        for i in range(2, num):
            if num % i == 0:
                total += i

        return total == num:
                total += i

        return total == num


        # 方法二：数学枚举
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        return num == 6 or num == 28 or num == 496 or num == 8128 or num == 33550336


        # 方法三：模拟2
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        if num <= 1:
            return False

        total = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                #print('i:', i)
                total += i
                if i * i != num:
                    #print('num % i:', num // i)
                    total += num // i
            i += 1

        #print(total)
        return total == num


    
    
    

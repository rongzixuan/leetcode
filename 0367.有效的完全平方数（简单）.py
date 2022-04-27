"""
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。

示例 1：
输入：num = 16
输出：true

示例 2：
输入：num = 14
输出：false
 
提示：
1 <= num <= 2^31 - 1

"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:


        # 方法一：二分法
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            #print(left, right)
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1

        return False


        # 方法二：牛顿迭代法
        # 时间复杂度：O(log4n)
        # 空间复杂度：O(1)
        x0 = num
        while True:
            x1 = (x0 + num / x0) / 2
            #print('x1:', x1)
            if abs(num - x1 * x1) < 1e-6:
                break
            x0 = x1
            #print(x0)

        return int(x0) * int(x0) == num
            






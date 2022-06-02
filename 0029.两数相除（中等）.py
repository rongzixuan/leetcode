"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:


        # 方法一：二分法
        # 时间复杂度：O(logC * logC)
        # 空间复杂度：O(1)
        if dividend == 0:
            return 0

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == INT_MIN:
            if divisor == -1:
                return INT_MAX
            elif divisor == 1:
                return INT_MIN

        if divisor == INT_MIN:
            if dividend == INT_MIN:
                return 1
            else:
                return 0

        reverse = False
        if dividend > 0:
            dividend = -dividend
            reverse = not reverse
        if divisor > 0:
            divisor = -divisor
            reverse = not reverse
        #print('dividend, divisor:', dividend, divisor)

        def getResult(mid):
            result = 0
            add = divisor
            while mid:
                #print(mid)
                if (mid & 1) == 1:
                    if result < dividend - add:
                        return False
                    result += add
                if mid != 1:
                    if add < dividend - add:
                        return False
                    add += add
                mid >>= 1
            return True

        left, right = 1, INT_MAX
        ans = 0
        while left <= right:
            #print('left, right:', left, right)
            mid = left + ((right - left) >> 1)
            #print('mid:', mid)
            check = getResult(mid)
            #print('check:', check)
            if check:
                ans = mid
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1

        return ans if not reverse else -ans

       

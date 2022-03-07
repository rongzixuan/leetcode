"""
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

 

示例 1:
输入: num = 100
输出: "202"

示例 2:
输入: num = -7
输出: "-10"
 

提示：
-10^7 <= num <= 10^7

"""


class Solution:
    def convertToBase7(self, num: int) -> str:


        # 方法一：模拟
        # 时间复杂度：O(log(num))
        # 空间复杂度：O(1)
        ans = 0
        i = 0
        flag = False if num >= 0 else True
        num = abs(num)
        while num:
            ans += (num % 7) * (10 ** i)
            num //= 7
            i += 1

        return '-' + str(ans) if flag else str(ans)
        
        

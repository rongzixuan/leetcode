"""
给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。


示例 1:
输入：n = 2
输出：987
解释：99 x 91 = 9009, 9009 % 1337 = 987

示例 2:
输入： n = 1
输出： 9
 

提示:
1 <= n <= 8

"""

class Solution:
    def largestPalindrome(self, n: int) -> int:


        # 方法一：暴力法（超时）
        # 时间复杂度：O(10^2n)
        # 空间复杂度：O()
        if n == 1:
            return 9

        min_num, max_num = 10 ** (n - 1), 10 ** n - 1
        #print(min_num, max_num)
        
        ans = 0
        for num1 in range(max_num, min_num - 1, -1):
            num2 = num1
            while num2 >= min_num:
                tmp_num = num1 * num2
                tmp_length = len(str(tmp_num))
                #print(num1, num2, tmp_num)

                if tmp_length % 2 == 0:
                    if int(
                        str(tmp_num)[: (tmp_length + 1) // 2] \
                      + str(tmp_num)[: (tmp_length + 1) // 2][::-1] \
                    ) == tmp_num:                        
                        #print(num1, num2, tmp_num)
                        ans = max(ans, tmp_num)
                    num2 -= 1
                else:
                    if int(
                        str(tmp_num)[: (tmp_length + 1) // 2] \
                      + str(tmp_num)[: (tmp_length + 1) // 2 - 1][::-1] \
                    ) == tmp_num:                        
                        #print(num1, num2, tmp_num)
                        ans = max(ans, tmp_num)
                    num2 -= 1

        return ans % 1337





"""
给你一个 正 整数 num ，输出它的补数。补数是对该数的二进制表示取反。

"""


class Solution:
    def findComplement(self, num: int) -> int:


        # 方法一：位运算
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        res = 0
        i = 0
        while num:
            tmp = 1 - (num & 1)
            #print(num, tmp)
            res += tmp * 2 ** i
            i += 1
            num >>= 1

        return res




        

"""
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

"""

class Solution:
    def countDigitOne(self, n: int) -> int:

        # 方法一：数学、枚举
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        if n == 0:
            return 0

        count = 0
        length = len(str(n))
        index = 0

        while index < length:
            count += (n//10**(index+1))*10**index \
                + min(max(0, (n%10**(index+1))-10**index+1), 10**index)
            #print(count)
            index += 1


        return count

    
    
    

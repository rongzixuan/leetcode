"""

给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

如果小数部分为循环小数，则将循环的部分括在括号内。

如果存在多个答案，只需返回 任意一个 。

对于所有给定的输入，保证 答案字符串的长度小于 104 。

"""



class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:


        # 方法一：数学模拟 + 哈希表
        # 时间复杂度：O(n)，n为答案字符串的长度
        # 空间复杂度：O(n)
        if numerator == 0:
            return "0"
        elif numerator == denominator:
            return "1"
        elif (numerator // denominator * denominator) == numerator:   # 可以整除
        #elif numerator % denominator == 0:
            return str(numerator // denominator)

        res = ""
        if numerator * denominator < 0:  # 负数
            res += "-"
            numerator, denominator = abs(numerator), abs(denominator)

        res += str(numerator // denominator) 
        res += "."  # 整数部分
        numerator %= denominator
        hash_table = {}  # 记录出现过的小数部分的数字
        #print('numerator:', numerator)

        while numerator:
            if numerator not in hash_table:
                hash_table[numerator] = len(res)
                numerator *= 10
                res += str(numerator // denominator)              
                numerator %= denominator
            else:
                index = hash_table[numerator]
                res = res[0: index] + "(" + res[index:] + ")"
                #print(hash_table)
                return res
              
        return res





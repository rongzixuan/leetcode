"""
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:
十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法

"""

class Solution:
    def toHex(self, num: int) -> str:


        # 方法一：位运算
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        res = ""
        if 0 <= num < 10:
            return str(num)

        hash_table = {10: 'a',
                      11: 'b',
                      12: 'c',
                      13: 'd',
                      14: 'e',
                      15: 'f'}

        while num and len(res) < 8:
            if 10 <= num % 16 < 16:
                res += hash_table[num % 16]
            else:
                res += str(num % 16)
            #num //= 16
            num >>= 4

        #print('res before:', res)
        res = res[::-1]
        #print('res after:', res)

        #if num < 0:

        return res

        
              

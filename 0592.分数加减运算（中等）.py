"""
给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。 
这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。

示例 1:
输入: expression = "-1/2+1/2"
输出: "0/1"

示例 2:
输入: expression = "-1/2+1/2+1/3"
输出: "1/3"

示例 3:
输入: expression = "1/3-1/2"
输出: "-1/6"
 
提示:
输入和输出字符串只包含 '0' 到 '9' 的数字，以及 '/', '+' 和 '-'。 
输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 '+' 会被省略掉。
输入只包含合法的最简分数，每个分数的分子与分母的范围是  [1,10]。 如果分母是1，意味着这个分数实际上是一个整数。
输入的分数个数范围是 [1,10]。
最终结果的分子与分母保证是 32 位整数范围内的有效整数。

"""

class Solution:
    def fractionAddition(self, expression: str) -> str:


        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        def gongyue(a, b):
            while(b != 0):
                temp = a % b
                a = b
                b = temp
            return a

        def gongbei(a,b):
            return a * b // gongyue(a, b)

        numerator, denomirator = 0, 1     # 分子和分母
        tmp_numerator = 0
        tmp_denomirator = 0 if expression[0].isdigit() else 1
        tmp_signal = 1   # 正负号
        numerator_flag = 1  # 是否是分子
        n = len(expression)
        for i in range(n + 1):
            if i < n:
                ch = expression[i]
            else:
                ch = '#'
            #print('i, ch:', i, ch)
            if ch.isdigit():
                if numerator_flag > 0:
                    tmp_numerator = tmp_numerator * 10 + int(ch)
                else:
                    tmp_denomirator = tmp_denomirator * 10 + int(ch)
            elif i > 0:
                numerator_flag *= -1
            if ch == '+' or ch == '-' or ch == '#':
                lcm = gongbei(denomirator, tmp_denomirator)
                numerator *= lcm // denomirator
                tmp_numerator *= tmp_signal * lcm // tmp_denomirator 
                denomirator = lcm
                numerator += tmp_numerator
                tmp_numerator, tmp_denomirator = 0, 0
                if ch == '+':
                    tmp_signal = 1 
                elif ch == '-':
                    tmp_signal = -1
            #print('tmp_numerator, tmp_denomirator:', tmp_numerator, tmp_denomirator)
            #print('numerator, denomirator:', numerator, denomirator)     

        gcd = gongyue(numerator, denomirator)
        numerator //= gcd
        denomirator //= gcd
        return str(numerator) + '/' + str(denomirator)






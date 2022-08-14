"""
求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。
如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。
题目保证，如果方程中只有一个解，则 'x' 的值是一个整数。

示例 1：
输入: equation = "x+5-3+x=6+x-2"
输出: "x=2"

示例 2:
输入: equation = "x=x"
输出: "Infinite solutions"

示例 3:
输入: equation = "2x=x"
输出: "x=0" 

提示:
3 <= equation.length <= 1000
equation 只有一个 '='. 
方程由绝对值在 [0, 100]  范围内且无任何前导零的整数和变量 'x' 组成。

"""

class Solution:
    def solveEquation(self, equation: str) -> str:


        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        import re
        left, right = equation.split('=')[0], equation.split('=')[1]
        if left[0] == '-':
            left = '0x' + left
        else:
            left = '0x+' + left
        if right[0] == '-':
            right = '0x' + right
        else:
            right = '0x+' + right
        left = left.replace('-', '+-')
        right = right.replace('-', '+-')
        #print(left, right)
        #left_list = re.split(r'[+]', left)
        left_list = left.split('+')
        right_list = re.split(r'[+]', right)
        #print(left_list, right_list)
        #print(int('-2'))
        #print(int('-1'))
        #print(int('2'))

        co1, co2 = 0, 0
        for ch in left_list:
            print(ch)
            if 'x' not in ch:
                co2 -= int(ch)
            else:
                if ch == 'x':
                    co1 += 1
                elif ch == '-x':
                    co1 += -1
                else:
                    co1 += int(ch[:-1])

        for ch in right_list:
            #print(ch)
            if 'x' not in ch:
                co2 += int(ch)
            else:
                if ch == 'x':
                    co1 -= 1
                elif ch == '-x':
                    co1 -= -1
                else:
                    co1 -= int(ch[:-1])
        #print(co1, co2)

        if co1 == 0 and co2 != 0:
            return "No solution"
        elif co1 == 0 and co2 == 0:
            return "Infinite solutions"
        else:
            return  'x=' + str(int(co2 // co1))





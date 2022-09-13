"""
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :
输入: 2736
输出: 7236
解释: 交换数字2和数字7。

示例 2 :
输入: 9973
输出: 9973
解释: 不需要交换。

注意:
给定数字的范围是 [0, 10^8]

"""

class Solution:
    def maximumSwap(self, num: int) -> int:


        # 方法一：排序 + 遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if num == 0:
            return 0

        s = str(num)
        if len(s) < 2:
            return num

        num1 = list(s)
        #print(num1)
        num2 = sorted(s, reverse=True)
        #print(num2)    
        if num1 == num2:
            return num

        id1, id2 = 0, 0
        target = -1
        n = len(num1)
        for i in range(n):
            x, y = int(num1[i]), int(num2[i])
            #print(x, y)
            if target != -1 and x == target:
                #print('i:', i)
                id2 = i
            if target == -1 and x != y:
                id1 = i
                target = y

        #print(id1, id2)
        num1[id1], num1[id2] = num1[id2], num1[id1]
        return int("".join(num1))



         

"""
给定四个整数 sx , sy ，tx 和 ty，如果通过一系列的转换可以从起点 (sx, sy) 到达终点 (tx, ty)，则返回 true，否则返回 false。

从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。

示例 1:
输入: sx = 1, sy = 1, tx = 3, ty = 5
输出: true
解释:
可以通过以下一系列转换从起点转换到终点：
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

示例 2:
输入: sx = 1, sy = 1, tx = 2, ty = 2 
输出: false

示例 3:
输入: sx = 1, sy = 1, tx = 1, ty = 1 
输出: true

提示:
1 <= sx, sy, tx, ty <= 10^9

"""


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:


        # 方法一：辗转相减法（超时）
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        while tx >= sx or ty >= sy:
            if tx == 0 or ty == 0:
                return False
            elif tx == sx and ty == sy:
                return True

            if tx > ty:
                tx -= ty
            else:
                ty -= tx
            #print(tx, ty)
            

        return False


        # 方法二：辗转相除法
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        if tx < sx or ty < sy:
            return False

        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx 
            #print(tx, ty)

        if tx == sx and ty == sy:
            return True
        elif tx == sx:
            if (ty - sy) % tx == 0:
                return True
        elif ty == sy and (tx - sx) % ty == 0:
            return True          
        return False 











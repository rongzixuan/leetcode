"""
给定2D空间中四个点的坐标 p1, p2, p3 和 p4，如果这四个点构成一个正方形，则返回 true 。
点的坐标 pi 表示为 [xi, yi] 。输入 不是 按任何顺序给出的。
一个 有效的正方形 有四条等边和四个等角(90度角)。

示例 1:
输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
输出: True

示例 2:
输入：p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
输出：false

示例 3:
输入：p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
输出：true

提示:
p1.length == p2.length == p3.length == p4.length == 2
-10^4 <= xi, yi <= 10^4

"""

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:


        # 方法一：数学
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        def getDist(a, b):
            x1, y1 = a[0], a[1]
            x2, y2 = b[0], b[1]
            return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

        dist_list = []
        dist12 = getDist(p1, p2)
        dist13 = getDist(p1, p3)
        dist14 = getDist(p1, p4)
        dist23 = getDist(p2, p3)
        dist24 = getDist(p2, p4)
        dist34 = getDist(p3, p4)
        dist_list.extend([dist12, dist13, dist14, dist23, dist24, dist34])
        dist_list.sort()
        #print(dist_list)

        return True if dist_list[-1] == dist_list[-2] and dist_list[0] == dist_list[3] and dist_list[3] < dist_list[-2] else False





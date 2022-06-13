"""
给你 二维 平面上两个 由直线构成的 矩形，请你计算并返回两个矩形覆盖的总面积。

每个矩形由其 左下 顶点和 右上 顶点坐标表示：
第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。
第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义。

"""

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:


        # 方法一：数学
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        intersection_x = min(max(ax2 - bx1, 0), max(bx2 - ax1, 0), (ax2 - ax1), (bx2 - bx1))
        intersection_y = min(max(ay2 - by1, 0), max(by2 - ay1, 0), (ay2 - ay1), (by2 - by1))

        return area1 + area2 - intersection_x * intersection_y
        
        

"""
给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，如果这些点构成一个 回旋镖 则返回 true 。
回旋镖 定义为一组三个点，这些点 各不相同 且 不在一条直线上 。

示例 1：
输入：points = [[1,1],[2,3],[3,2]]
输出：true

示例 2：
输入：points = [[1,1],[2,2],[3,3]]
输出：false
 
提示：
points.length == 3
points[i].length == 2
0 <= xi, yi <= 100

"""

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:


        # 方法一：数学（角度）
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        if points[0] == points[1] or points[0] == points[2] or points[2] == points[1]:
            return False
        x1, y1 = points[0][0], points[0][1]
        x2, y2 = points[1][0], points[1][1]
        x3, y3 = points[2][0], points[2][1]

        import math
        angle1 = math.atan((y2 - y1) / (x2 - x1)) if x2 != x1 else float('inf')
        angle2 = math.atan((y3 - y2) / (x3 - x2)) if x2 != x3 else float('inf')

        return angle1 != angle2


        # 方法二：数学（斜率）
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        x1, y1 = points[0][0], points[0][1]
        x2, y2 = points[1][0], points[1][1]
        x3, y3 = points[2][0], points[2][1]

        return (x2 - x1) * (y3 - y2) != (y2 - y1) * (x3 - x2)


        # 方法三：数学（向量叉乘求面积）
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        v1 = (points[1][0] - points[0][0], points[1][1] - points[0][1])
        v2 = (points[2][0] - points[0][0], points[2][1] - points[0][1])
        return v1[0] * v2[1] - v1[1] * v2[0] != 0


        # 方法四：数学（求面积）
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        x1, y1 = points[0][0], points[0][1]
        x2, y2 = points[1][0], points[1][1]
        x3, y3 = points[2][0], points[2][1]

        return (x1*y2-x2*y1)+(x2*y3-x3*y2)+(x3*y1-x1*y3) != 0


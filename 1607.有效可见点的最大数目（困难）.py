"""
给你一个点数组 points 和一个表示角度的整数 angle ，你的位置是 location ，其中 location = [posx, posy] 且 points[i] = [xi, yi] 都表示 X-Y 平面上的整数坐标。

最开始，你面向东方进行观测。你 不能 进行移动改变位置，但可以通过 自转 调整观测角度。换句话说，posx 和 posy 不能改变。你的视野范围的角度用 angle 表示， 这决定了你观测任意方向时可以多宽。设 d 为你逆时针自转旋转的度数，那么你的视野就是角度范围 [d - angle/2, d + angle/2] 所指示的那片区域。

对于每个点，如果由该点、你的位置以及从你的位置直接向东的方向形成的角度 位于你的视野中 ，那么你就可以看到它。

同一个坐标上可以有多个点。你所在的位置也可能存在一些点，但不管你的怎么旋转，总是可以看到这些点。同时，点不会阻碍你看到其他点。

返回你能看到的点的最大数目。

示例 1：
输入：points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
输出：3
解释：阴影区域代表你的视野。在你的视野中，所有的点都清晰可见，尽管 [2,2] 和 [3,3]在同一条直线上，你仍然可以看到 [3,3] 。

示例 2：
输入：points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
输出：4
解释：在你的视野中，所有的点都清晰可见，包括你所在位置的那个点。

示例 3：
输入：points = [[1,0],[2,1]], angle = 13, location = [1,1]
输出：1
解释：如图所示，你只能看到两点之一。

提示：
1 <= points.length <= 10^5
points[i].length == 2
location.length == 2
0 <= angle < 360
0 <= posx, posy, xi, yi <= 100

"""

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        """sameCnt = 0
        polarDegrees = []
        for p in points:
            if p == location:
                sameCnt += 1
            else:
                polarDegrees.append(atan2(p[1] - location[1], p[0] - location[0]))
        polarDegrees.sort()
        print('polarDegrees:', polarDegrees)

        n = len(polarDegrees)
        polarDegrees += [deg + 2 * pi for deg in polarDegrees]
        print('polarDegrees:', polarDegrees)

        degree = angle * pi / 180
        print('degree:', degree)
        maxCnt = max((bisect_right(polarDegrees, polarDegrees[i] + degree) - i for i in range(n)), default=0)
        return maxCnt + sameCnt"""


        # 方法一：数学 + 二分法
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(points)
        angle_pi = angle * pi / 180
        #print(angle_pi)

        points_angle = []
        same_point = 0
        for point in points:
            if point == location:
                same_point += 1
            else:
                tmp_angle = atan2(point[1] - location[1], point[0] - location[0])
                points_angle.append(tmp_angle)
        #print('same_point:', same_point)
        points_angle.sort()
        #print(points_angle)
        points_angle += [deg + 2 * pi for deg in points_angle]
        #points_angle = [tmp + 2 * pi for tmp in points_angle]  # 防止出现负数
        #print(points_angle)

        max_points = 0
        m = len(points_angle)
        for i in range(m):
            target = points_angle[i] + angle_pi
            #print('target:', target)
            left, right = 0, m - 1

            while left <= right:
                #print('i, left, right:', i, left, right)
                mid = left + (right - left) // 2
                #print('mid:', mid)
                if points_angle[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            max_points = max(max_points, right + 1 - i)

        return max_points + same_point


        # 方法二：数学 + 滑动窗口
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(points)
        angle_pi = angle * pi / 180
        #print(angle_pi)

        points_angle = []
        same_point = 0
        for point in points:
            if point == location:
                same_point += 1
            else:
                tmp_angle = atan2(point[1] - location[1], point[0] - location[0])
                points_angle.append(tmp_angle)
        #print('same_point:', same_point)
        points_angle.sort()
        #print(points_angle)
        points_angle += [deg + 2 * pi for deg in points_angle]
        #points_angle = [tmp + 2 * pi for tmp in points_angle]  # 防止出现负数
        #print(points_angle)

        max_points = 0
        m = len(points_angle)
        max_points = 0
        j = 0
        for i in range(m):
            while j < m and points_angle[j] - points_angle[i] <= angle_pi:
                j += 1
            max_points = max(max_points, j - i)
        return max_points + same_point


    
    
    

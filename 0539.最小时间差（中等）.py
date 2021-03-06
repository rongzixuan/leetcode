"""
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。

示例 1：
输入：timePoints = ["23:59","00:00"]
输出：1

示例 2：
输入：timePoints = ["00:00","23:59","00:00"]
输出：0
 
提示：
2 <= timePoints.length <= 2 * 10^4
timePoints[i] 格式为 "HH:MM"

"""


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:


        # 方法一：排序
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        def getMinutes(str1, str2):
            time1 = int(str1[:2]) * 60 + int(str1[3:])
            time2 = int(str2[:2]) * 60 + int(str2[3:])
            if time1 > time2:
                time2 += 1440
            return time2 - time1

        timePoints.sort()
        #print(timePoints)
        if timePoints[0] == timePoints[-1]:
            return 0
        n = len(timePoints)

        min_sub = getMinutes(timePoints[-1], timePoints[0])
        for i in range(1, n):
            if timePoints[i] == timePoints[i - 1]:
                return 0
            tmp_sub = getMinutes(timePoints[i - 1], timePoints[i])
            min_sub = min(min_sub, tmp_sub)

        return min_sub







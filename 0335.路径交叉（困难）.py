"""
给你一个整数数组 distance 。
从 X-Y 平面上的点 (0,0) 开始，先向北移动 distance[0] 米，然后向西移动 distance[1] 米，向南移动 distance[2] 米，向东移动 distance[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。

判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。

"""

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:


        # 方法一：归纳法（相交的情况）
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(distance)
        if n < 4:
            return False

        for i in range(3, n):
            if distance[i] >= distance[i-2] \
            and distance[i-1] <= distance[i-3]:
                #print('i:', i)
                print('1')
                return True

            if i >= 4 \
            and distance[i-1] == distance[i-3] \
            and distance[i] + distance[i-1] >= distance[i-2]:
                print('11')
                return True

            if i >= 5 \
            and distance[i-1] + distance[i-5] >= distance[i-3] \
            and distance[i-3] > distance[i-5] \
            and distance[i-1] <= distance[i-3] \
            and distance[i-4] < distance[i-2] \
            and distance[i-4] + distance[i] >= distance[i-2]:
                print('111')
                return True

        return False


        # 方法二：归纳法2（不相交的情况）
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(distance)
        if n < 4:
            return False

        i = 2
        # 向外卷
        while i < n and distance[i] > distance[i-2]:
            i += 1

        if i == n:
            return False

        # 外卷转内卷
        if (i == 3 and distance[i] == distance[i-2]) \
        or (i >= 4 and distance[i] >= distance[i-2] - distance[i-4]):
            distance[i-1] -= distance[i-3] # 剪裁

        i += 1
        while i < n and distance[i] < distance[i-2]:
            i += 1

        return i != n




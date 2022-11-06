"""
给你一个数组 towers 和一个整数 radius 。
数组  towers  中包含一些网络信号塔，其中 towers[i] = [xi, yi, qi] 表示第 i 个网络信号塔的坐标是 (xi, yi) 且信号强度参数为 qi 。所有坐标都是在  X-Y 坐标系内的 整数 坐标。两个坐标之间的距离用 欧几里得距离 计算。
整数 radius 表示一个塔 能到达 的 最远距离 。如果一个坐标跟塔的距离在 radius 以内，那么该塔的信号可以到达该坐标。在这个范围以外信号会很微弱，所以 radius 以外的距离该塔是 不能到达的 。
如果第 i 个塔能到达 (x, y) ，那么该塔在此处的信号为 ⌊qi / (1 + d)⌋ ，其中 d 是塔跟此坐标的距离。一个坐标的 信号强度 是所有 能到达 该坐标的塔的信号强度之和。

请你返回数组 [cx, cy] ，表示 信号强度 最大的 整数 坐标点 (cx, cy) 。如果有多个坐标网络信号一样大，请你返回字典序最小的 非负 坐标。

注意：
坐标 (x1, y1) 字典序比另一个坐标 (x2, y2) 小，需满足以下条件之一：
要么 x1 < x2 ，
要么 x1 == x2 且 y1 < y2 。
⌊val⌋ 表示小于等于 val 的最大整数（向下取整函数）。

示例 1：
输入：towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
输出：[2,1]
解释：
坐标 (2, 1) 信号强度之和为 13
- 塔 (2, 1) 强度参数为 7 ，在该点强度为 ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
- 塔 (1, 2) 强度参数为 5 ，在该点强度为 ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
- 塔 (3, 1) 强度参数为 9 ，在该点强度为 ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
没有别的坐标有更大的信号强度。

示例 2：
输入：towers = [[23,11,21]], radius = 9
输出：[23,11]
解释：由于仅存在一座信号塔，所以塔的位置信号强度最大。

示例 3：
输入：towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
输出：[1,2]
解释：坐标 (1, 2) 的信号强度最大。
 
提示：
1 <= towers.length <= 50
towers[i].length == 3
0 <= xi, yi, qi <= 50
1 <= radius <= 50

"""

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:


        # 方法一：枚举
        # 时间复杂度：O(nlogn + n * radius * radius)
        # 空间复杂度：O(max_x * max_y)
        n = len(towers)
        towers.sort(key = lambda x: x[0])
        #print(towers)
        min_x, max_x = towers[0][0] - radius, towers[-1][0] + 2 * radius
        towers.sort(key = lambda x: x[1])
        min_y, max_y = towers[0][1] - radius, towers[-1][1] + 2 * radius
        #print(min_x, min_y, max_x, max_y)
        res = [[0 for j in range(max_y + 1)] for i in range(max_x + 1)]
        #print(res)

        for x, y, q in towers:
            for new_x, new_y in product(range(x - radius, x + radius + 1), range(y - radius, y + radius + 1)):
                #print('new_x, new_y:', new_x, new_y)
                d = ((x - new_x) ** 2 + (y - new_y) ** 2) ** 0.5
                if 0 <= new_x and 0 <= new_y and d <= radius:
                    p = int(q / (1 + d))
                    #print('p:', p)
                    res[new_x][new_y] += p
        #print(res)

        max_res = 0
        ans = [0, 0]
        for i in range(max_x + 1):
            for j in range(max_y + 1):
                if res[i][j] > max_res:
                    max_res = res[i][j]
                    ans = [i, j]
        return ans


        

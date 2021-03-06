"""
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
在加热器的加热半径范围内的每个房屋都可以获得供暖。
现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。

示例 1:
输入: houses = [1,2,3], heaters = [2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。

示例 2:
输入: houses = [1,2,3,4], heaters = [1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。

示例 3：
输入：houses = [1,5], heaters = [2]
输出：3
 
提示：
1 <= houses.length, heaters.length <= 3 * 10^4
1 <= houses[i], heaters[i] <= 10^9

"""

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:


        # 方法一：排序 + 二分法
        # 时间复杂度：O(nlogn + mlogn)
        # 空间复杂度：O(1)
        m, n = len(houses), len(heaters)

        from bisect import bisect_left, bisect_right
        max_dis = 0
        heaters.sort()
        for house in houses:
            #left = bisect_left(heaters, house)
            right = bisect_right(heaters, house)
            #right = left + 1
            left = right - 1
            #print(left, right)
            left_dis = house - heaters[left] if left >= 0 else float('inf')    
            right_dis = heaters[right] - house if right < n else float('inf')           
            max_dis = max(max_dis, min(left_dis, right_dis))

        return max_dis


        # 方法二：排序 + 双指针
        # 时间复杂度：O(mlogm + nlogn + m)
        # 空间复杂度：O(1)
        m, n = len(houses), len(heaters)
        houses.sort()
        heaters.sort()

        left, right = 0, 0
        max_dis = 0
        for house in houses:
            #print('before:', left, right)
            while left < n and heaters[left] < house:
                left += 1
            left -= 1           
            while right < n and heaters[right] < house:
                right += 1
            #print('after:', left, right)
            left_dis = house - heaters[left] if left >= 0 else float('inf')
            right_dis = heaters[right] - house if right < n else float('inf')
            #print(left_dis, right_dis)
            max_dis = max(max_dis, min(left_dis, right_dis))

            left = 0 if left == -1 else left

        return max_dis





"""
给你一个整数数组 nums 。你可以选定任意的 正数 startValue 作为初始值。
你需要从左到右遍历 nums 数组，并将 startValue 依次累加上 nums 数组中的值。
请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 正数 作为 startValue 。

示例 1：
输入：nums = [-3,2,-3,4,2]
输出：5
解释：如果你选择 startValue = 4，在第三次累加时，和小于 1 。
                累加求和
                startValue = 4 | startValue = 5 | nums
                  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
                  
示例 2：
输入：nums = [1,2]
输出：1
解释：最小的 startValue 需要是正数。

示例 3：
输入：nums = [1,-2,-3]
输出：5
 
提示：
1 <= nums.length <= 100
-100 <= nums[i] <= 100

"""

class Solution:
    def minStartValue(self, nums: List[int]) -> int:


        # 方法一：贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        """min_sum = float('inf')
        tmp_sum = 0
        for num in nums:
            tmp_sum += num
            min_sum = min(min_sum, tmp_sum)

        return abs(min_sum) + 1 if min_sum <= 0 else 1"""


        # 方法二：二分法
        # 时间复杂度：O(logn * n)
        # 空间复杂度：O(1)
        if min(nums) > 0:
            return 1

        def check(mid):
            for num in nums:
                mid += num
                if mid <= 0:
                    return False
            return True

        left, right = 1, abs(sum([num for num in nums if num < 1])) + 1
        #print(left, right)
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left






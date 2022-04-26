"""
给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。

如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。


示例 1：
输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意

示例 2：
输入：nums = [5,4,3,2,1]
输出：false
解释：不存在满足题意的三元组

示例 3：
输入：nums = [2,1,5,0,4,6]
输出：true
解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
 

提示：
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1

进阶：你能实现时间复杂度为 O(n) ，空间复杂度为 O(1) 的解决方案吗？

"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:


        # 方法一：贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n < 3:
            return False

        first, second = float(inf), float(inf)
        for num in nums:
            if num > first and num > second:
                return True
            elif num < first:
                first = num
            elif num > first and num < second:
                second = num

        return False


        # 方法二：双向遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        if n < 3:
            return False

        left_min = []
        min_num = float('inf')
        for num in nums:
            if num < min_num:
                min_num = num
            left_min.append(min_num)
        #print(left_min)

        right_max = [0] * n
        max_num = float('-inf')
        for i in range(n - 1, -1, -1):
            if nums[i] > max_num:
                max_num = nums[i]
            right_max[i] = max_num
        #print(right_max)

        for i, num in enumerate(nums):
            if left_min[i] < num and num < right_max[i]:
                return True

        return False




        

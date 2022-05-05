"""
给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
 
示例 1：
输入：nums = [10,5,2,6], k = 100
输出：8
解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。

示例 2：
输入：nums = [1,2,3], k = 0
输出：0
 
提示: 
1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6

"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:


        # 方法一：双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)

        count = 0
        product = 1
        left = 0
        for right in range(n):
            product *= nums[right]
            while left < right and product >= k:               
                product /= nums[left]
                left += 1
            #print(left, right, product)
            if product < k:
                count += (right - left + 1)

        return count


        # 方法二：二分查找
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        if k == 0:
            return 0

        n = len(nums)
        log_prefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            log_prefix[i + 1] = log_prefix[i] + log(num)

        count = 0
        for right in range(0, n):
            left = bisect_right(log_prefix, log_prefix[right + 1] - log(k) + 1e-10, 0, right + 1)
            count += (right - left + 1)

        return count












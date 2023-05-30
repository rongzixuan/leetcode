"""
给你一个由正整数组成的整数数组 nums ，返回其中可被 3 整除的所有偶数的平均值。

注意：n 个元素的平均值等于 n 个元素 求和 再除以 n ，结果 向下取整 到最接近的整数。

示例 1：
输入：nums = [1,3,6,10,12,15]
输出：9
解释：6 和 12 是可以被 3 整除的偶数。(6 + 12) / 2 = 9 。

示例 2：
输入：nums = [1,2,4,7,10]
输出：0
解释：不存在满足题目要求的整数，所以返回 0 。
 
提示：
1 <= nums.length <= 1000
1 <= nums[i] <= 1000

  """
  
  class Solution:
    def averageValue(self, nums: List[int]) -> int:


        # 方法一：遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        total = 0
        count = 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                total += num
                count += 1
        return total // count if count > 0 else 0


"""
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。

如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

示例 1：
输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。

示例 2：
输入：nums = [5,6,7,8,9], x = 4
输出：-1

示例 3：
输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。

提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9

"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:


        # 方法一：滑动窗口
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if nums[0] > x and nums[-1] > x:
            return -1 

        total = sum(nums)
        #print(total)
        total_mid = 0
        target = total - x
        #print(target)
        if target < 0:
            return -1
        left = 0
        ans = -1
        for right, num in enumerate(nums):
            total_mid += num
            while total_mid > target:
                total_mid -= nums[left]
                left += 1
            if total_mid == target:
                ans = max(ans, right - left + 1)

        #print(total_mid)
        return n - ans if ans >= 0 else -1


        # 方法二：前缀和 + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        count = {0: -1}
        ans = inf
        target = sum(nums) - x
        tmp_sum = 0
        for right, num in enumerate(nums):
            tmp_sum += num
            if tmp_sum not in count:
                count[tmp_sum] = right
            if tmp_sum - target in count:
                left = count[tmp_sum - target]
                ans = min(ans, n - right + left)          
        return ans if ans != inf else -1





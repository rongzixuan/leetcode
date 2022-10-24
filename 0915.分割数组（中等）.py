"""
给定一个数组 nums ，将其划分为两个连续子数组 left 和 right， 使得：
left 中的每个元素都小于或等于 right 中的每个元素。
left 和 right 都是非空的。
left 的长度要尽可能小。

在完成这样的分组后返回 left 的 长度 。

用例可以保证存在这样的划分方法。

示例 1：
输入：nums = [5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]

示例 2：
输入：nums = [1,1,1,0,6,12]
输出：4
解释：left = [1,1,1,0]，right = [6,12]
 
提示：
2 <= nums.length <= 10^5
0 <= nums[i] <= 10^6
可以保证至少有一种方法能够按题目所描述的那样对 nums 进行划分。

"""

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:


        # 方法一：两次遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        right_min = [n] * n
        tmp1 = inf
        for i in range(n - 1, -1, -1):
            tmp1 = min(tmp1, nums[i])
            right_min[i] = tmp1
        #print(right_min)

        tmp2 = 0
        for i in range(n - 1):
            tmp2 = max(tmp2, nums[i])
            if tmp2 <= right_min[i + 1]:
                return i + 1
        return n


        # 方法二：一次遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        cur_max, left_max = nums[0], nums[0]
        ans = 1
        for i in range(1, n):
            cur_max = max(cur_max, nums[i])
            if nums[i] < left_max:
                left_max = cur_max
                ans = i + 1
        return ans







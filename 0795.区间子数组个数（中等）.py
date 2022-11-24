"""
给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。
生成的测试用例保证结果符合 32-bit 整数范围。

示例 1：
输入：nums = [2,1,4,3], left = 2, right = 3
输出：3
解释：满足条件的三个子数组：[2], [2, 1], [3]

示例 2：
输入：nums = [2,9,2,5,6], left = 2, right = 8
输出：7

提示：
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= left <= right <= 10^9

"""

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:


        # 方法一：遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        mid1 = -1
        mid2 = -1
        big = -1  # 
        #small = 0
        ans = 0
        for i, num in enumerate(nums):
            if num >= left and num <= right:
                ans += (i - big)
                if mid1 == -1:
                    mid1 = i
                    mid2 = i
                else:
                    mid2 = i
            elif num < left:
                #smaller += 1
                if mid1 != -1 and mid2 != -1:
                    ans += (mid2 - big)
            elif num > right:
                big = i
                mid1 = -1
                mid2 = -1
        return ans


        # 方法二：遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        res = 0
        last2 = last1 = -1
        for i, x in enumerate(nums):
            if left <= x <= right:
                last1 = i
            elif x > right:
                last2 = i
                last1 = -1
            if last1 != -1:
                res += last1 - last2
        return res


        # 方法三：计数（容斥原理）
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        def count(lower: int) -> int:
            res = cur = 0
            for x in nums:
                if x <= lower:
                    cur += 1
                else:
                    cur = 0
                res += cur
            return res
        return count(right) - count(left - 1)






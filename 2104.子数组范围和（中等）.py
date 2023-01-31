"""
给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。

返回 nums 中 所有 子数组范围的 和 。

子数组是数组中一个连续 非空 的元素序列。

示例 1：
输入：nums = [1,2,3]
输出：4
解释：nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0 
[2]，范围 = 2 - 2 = 0
[3]，范围 = 3 - 3 = 0
[1,2]，范围 = 2 - 1 = 1
[2,3]，范围 = 3 - 2 = 1
[1,2,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4

示例 2：
输入：nums = [1,3,3]
输出：4
解释：nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0
[3]，范围 = 3 - 3 = 0
[3]，范围 = 3 - 3 = 0
[1,3]，范围 = 3 - 1 = 2
[3,3]，范围 = 3 - 3 = 0
[1,3,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4

示例 3：
输入：nums = [4,-2,-3,4,1]
输出：59
解释：nums 中所有子数组范围的和是 59
 
提示：
1 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
 
进阶：你可以设计一种时间复杂度为 O(n) 的解决方案吗？

"""


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:


        # 方法一：暴力法
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        n = len(nums)
        ans = 0
        for i in range(n - 1):
            max_num, min_num = nums[i], nums[i]
            for j in range(i + 1, n):
                max_num, min_num = max(max_num, nums[j]), min(min_num, nums[j])
                ans += (max_num - min_num)

        return ans


        # 方法二：单调栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        
        from collections import deque
        min_left_stack, max_left_stack = deque(), deque()    # 从左边遍历最小/大的元素栈
        min_left_index, max_left_index = [-1]  * n, [-1] * n # 左边最近的比自己小/大的元素       
        for i in range(n):
            while min_left_stack and nums[min_left_stack[-1]] > nums[i]:
                min_left_stack.pop()            
            min_left_index[i] = min_left_stack[-1] if min_left_stack else -1
            min_left_stack.append(i)

            while max_left_stack and nums[max_left_stack[-1]] <= nums[i]:
                max_left_stack.pop()
            max_left_index[i] = max_left_stack[-1] if max_left_stack else -1
            max_left_stack.append(i)           
        #print('min_left_index:', min_left_index)
        #print('max_left_index:', max_left_index)

        min_right_stack, max_right_stack = deque(), deque()    # 从右边遍历最小/大的元素栈
        min_right_index, max_right_index = [-1]  * n, [-1] * n # 右边最近的比自己小/大的元素       
        for i in range(n - 1, -1, -1):
            while min_right_stack and nums[min_right_stack[-1]] >= nums[i]:
                min_right_stack.pop()
            min_right_index[i] = min_right_stack[-1] if min_right_stack else n
            min_right_stack.append(i)
            
            while max_right_stack and nums[max_right_stack[-1]] < nums[i]:
                max_right_stack.pop()
            max_right_index[i] = max_right_stack[-1] if max_right_stack else n
            max_right_stack.append(i)            
        #print('min_right_index:', min_right_index)
        #print('max_right_index:', max_right_index)

        max_sum, min_sum = 0, 0
        for i in range(n):
            max_sum += (max_right_index[i] - i) * (i - max_left_index[i]) * nums[i]
            min_sum += (min_right_index[i] - i) * (i - min_left_index[i]) * nums[i]

        return max_sum - min_sum









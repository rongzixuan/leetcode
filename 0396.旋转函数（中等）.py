"""
给定一个长度为 n 的整数数组 nums 。

假设 arrk 是数组 nums 顺时针旋转 k 个位置后的数组，我们定义 nums 的 旋转函数  F 为：
F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]
返回 F(0), F(1), ..., F(n-1)中的最大值 。

生成的测试用例让答案符合 32 位 整数。

示例 1:
输入: nums = [4,3,2,6]
输出: 26
解释:
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。

示例 2:
输入: nums = [100]
输出: 0
 
提示:
n == nums.length
1 <= n <= 10^5
-100 <= nums[i] <= 100

"""


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:


        # 方法一：迭代
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)

        max_num = 0
        tmp_sum = 0
        total = 0
        for i, num in enumerate(nums):
            tmp_sum += i * num
            total += num
        max_num = tmp_sum
        #print(max_num)

        for j in range(n - 1, 0, -1):
            tmp_sum += (total - n * nums[j])
            max_num = max(max_num, tmp_sum)

        return max_num



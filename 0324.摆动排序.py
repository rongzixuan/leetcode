"""
给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
你可以假设所有输入数组都可以得到满足题目要求的结果。

示例 1：
输入：nums = [1,5,1,1,6,4]
输出：[1,6,1,5,1,4]
解释：[1,4,1,5,1,6] 同样是符合题目要求的结果，可以被判题程序接受。

示例 2：
输入：nums = [1,3,2,2,3,1]
输出：[2,3,1,3,1,2]
 
提示：
1 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 5000
题目数据保证，对于给定的输入 nums ，总能产生满足题目要求的结果

进阶：你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

"""

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 方法一：排序
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        tmp_nums = sorted(nums)
        #print(tmp_nums)
        n = len(nums)
        left = (n - 1) // 2
        right = n - 1

        for i in range(n):
            #print(i, left, right)
            if i % 2 == 0:
                nums[i] = tmp_nums[left]
                left -= 1
            else:
                nums[i] = tmp_nums[right]
                right -= 1


        # 方法二：排序（错误）
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        # excaple：[4,5,5,6]
        tmp_nums = sorted(nums)
        #print(tmp_nums)
        n = len(nums)
        left = 0
        right = (n + 1)// 2

        for i in range(n):
            #print(i, left, right)
            if i % 2 == 0:
                nums[i] = tmp_nums[left]
                left += 1
            else:
                nums[i] = tmp_nums[right]
                right += 1
                
                
                

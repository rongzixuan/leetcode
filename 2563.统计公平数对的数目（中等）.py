"""
给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。

如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：

0 <= i < j < n，且
lower <= nums[i] + nums[j] <= upper
 
示例 1：
输入：nums = [0,1,7,4,4,5], lower = 3, upper = 6
输出：6
解释：共计 6 个公平数对：(0,3)、(0,4)、(0,5)、(1,3)、(1,4) 和 (1,5) 。

示例 2：
输入：nums = [1,7,9,2,5], lower = 11, upper = 11
输出：1
解释：只有单个公平数对：(2,3) 。
 
提示：
1 <= nums.length <= 10^5
nums.length == n
-10^9 <= nums[i] <= 10^9
-10^9 <= lower <= upper <= 10^

"""

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        
        # 方法一：有序队列 + 二分法
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(nums)
        from bisect import bisect_right, bisect_left
        from sortedcontainers import SortedList
        pre = SortedList()
        ans = 0
        for i, num in enumerate(nums):
            if len(pre) > 0:
                if pre[0] > lower - num:
                    print('left1')
                    left = 0
                else:
                    left = bisect_left(pre, lower - num)
                if pre[-1] < upper - num:
                    print('right1')
                    right = len(pre)
                else:
                    right = bisect_right(pre, upper - num)
                #print('i, num, lower - num, upper - num, left, right:', i, num, lower - num, upper - num, left, right)
                ans += (right - left)
            pre.add(num)
        return ans
        
        
        # 方法二：排序 + 二分法
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        ans = 0
        nums.sort()
        for j, x in enumerate(nums):
            r = bisect_right(nums, upper - x, 0, j)
            l = bisect_left(nums, lower - x, 0, j)
            ans += r - l
        return ans
      
      
      
        
        
        
        

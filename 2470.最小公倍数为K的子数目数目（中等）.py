"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的 子数组 中满足 元素最小公倍数为 k 的子数组数目。
子数组 是数组中一个连续非空的元素序列。
数组的最小公倍数 是可被所有数组元素整除的最小正整数。

示例 1 ：
输入：nums = [3,6,2,7,1], k = 6
输出：4
解释：以 6 为最小公倍数的子数组是：
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]

示例 2 ：
输入：nums = [3], k = 2
输出：0
解释：不存在以 2 为最小公倍数的子数组。

提示：
1 <= nums.length <= 1000
1 <= nums[i], k <= 1000

"""

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        
        # 方法一：双指针（错误）
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        n = len(nums)
        #dp = [0] * n
        #tmp_max = 0
        tmp_index = []
        left = 0
        ans = 0
        flag = False
        for right in range(n):
            if k >= nums[right] and k % nums[right] == 0:
                #print('right:', right)
                if flag == False:
                    left = right
                    flag = True
                if nums[right] == k:
                    tmp_index.append(right)      
            if (right < n - 1 and k % nums[right + 1] != 0 and k >= nums[right] and k % nums[right] == 0) or right == n - 1:      
                #print('1:', left, right, tmp_index)
                if len(tmp_index) == 1:
                    ans += (tmp_index[0] - left + 1) * (right - tmp_index[0] + 1)
                elif len(tmp_index) > 1:
                    #print('2:', left, right, tmp_index)
                    for i, index in enumerate(tmp_index):
                        print(left, right, index)
                        if i == 0:
                            ans += (index - left + 1) * (tmp_index[i + 1] - index)
                        elif i == len(tmp_index) - 1:
                            ans += (index - tmp_index[i - 1]) * (right - index + 1)
                        else:
                            ans += (index - tmp_index[i - 1] + 1) * (tmp_index[i + 1] - index + 1)
                tmp_index = []
                left = -1
                flag = False
                
        return ans


        # 方法二：遍历
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        from math import lcm
        res = 0
        for i in range(len(nums)):
            lcm_ = 1
            for j in range(i, len(nums)):
                lcm_ = lcm(lcm_, nums[j])
                if lcm_ == k:
                    res += 1
        return res
      
      
      

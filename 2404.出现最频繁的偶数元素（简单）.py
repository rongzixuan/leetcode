"""
给你一个整数数组 nums ，返回出现最频繁的偶数元素。
如果存在多个满足条件的元素，只需要返回 最小 的一个。如果不存在这样的元素，返回 -1 。

示例 1：
输入：nums = [0,1,2,2,4,4,1]
输出：2
解释：
数组中的偶数元素为 0、2 和 4 ，在这些元素中，2 和 4 出现次数最多。
返回最小的那个，即返回 2 。

示例 2：
输入：nums = [4,4,4,9,2,4]
输出：4
解释：4 是出现最频繁的偶数元素。

示例 3：
输入：nums = [29,47,21,41,13,37,25,7]
输出：-1
解释：不存在偶数元素。
 
提示：
1 <= nums.length <= 2000
0 <= nums[i] <= 10^5

"""

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        
        # 2022/09/11
        # 方法一：哈希表
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        count = Counter(nums)
        count = sorted(count.items(), key = lambda x: [x[1], -x[0]], reverse=True)
        #print(count)
        
        for k, v in count:
            #print(k, v)
            if k % 2 == 0:
                return k
        return -1
    
    
        # 2023/04/13
        # 方法一：哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        from collections import Counter
        count = Counter(nums)
        ans = -1
        max_count = 0
        #print(count)

        for k, v in count.items():
            if k % 2 == 0: 
                if v > max_count:
                    max_count = v
                    ans = k
                elif v == max_count and ans != -1:
                    ans = min(ans, k)
        return ans
      
      
      
      

"""
给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。


示例 1：
输入：nums = [1,2,3,1], k = 3
输出：true

示例 2：
输入：nums = [1,0,1,1], k = 1
输出：true

示例 3：
输入：nums = [1,2,3,1,2,3], k = 2
输出：false
 
 
提示：
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5

"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        # 方法一：哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        from collections import defaultdict
        hash_table = defaultdict(list)

        for i, num in enumerate(nums):
            if num in hash_table:
                if i - hash_table[num][-1] <= k:
                    return True
            hash_table[num].append(i)

        return False


        # 方法二：滑动窗口
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        
        num_set = set()
        if n <= k:
            for i in range(n):
                if nums[i] in num_set:
                    #print('i:', i)
                    return True
                num_set.add(nums[i])
            return False

        for i in range(k + 1):
            if nums[i] in num_set:
                #print('i:', i)
                return True
            num_set.add(nums[i])
        #print(num_set)

        left, right = 1, k + 1
        num_set.remove(nums[0])
        #print(num_set)
        while right < n:
            #print('left, right, num_set:', left, right,num_set)
            if nums[right] in num_set:
                #print('right:', right)
                return True
            num_set.add(nums[right])
            num_set.remove(nums[left])
            left += 1
            right += 1

        return False









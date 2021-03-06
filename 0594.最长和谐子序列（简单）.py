"""
和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。
现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。
数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。

示例 1：
输入：nums = [1,3,2,2,5,2,3,7]
输出：5
解释：最长的和谐子序列是 [3,2,2,2,3]

示例 2：
输入：nums = [1,2,3,4]
输出：2

示例 3：
输入：nums = [1,1,1,1]
输出：0
 
提示：
1 <= nums.length <= 2 * 104
-10^9 <= nums[i] <= 10^9

"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:


        # 方法一：哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        if n == 1:
            return 0

        hash_table = defaultdict(list)
        max_length = 0
        for i in range(n):
            num = nums[i]
            length1 = len(hash_table[num - 1])
            length2 = len(hash_table[num + 1])
            hash_table[num].append(i)
            length3 = len(hash_table[num])
            if length1 or length2:
                max_length = max(max_length, max(length1, length2) + length3)
            #print(max_length)         

        #print(hash_table)
        return max_length


        # 方法二：排序 + 模拟
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        nums.sort()
        #print(nums)
        n = len(nums)
        if n == 1:
            return 0
      
        min_num, max_num = nums[0], nums[-1]
        if min_num == max_num:
            return 0
        elif min_num + 1 == max_num:
            return n

        max_length = 0
        j = 0
        for i in range(n):
            if nums[i] != max_num:
                while j + 1 < n and nums[j+1] - nums[i] < 2:
                    j += 1
                if nums[i] != nums[j]:
                    max_length = max(max_length, j - i + 1)
            #print(i, max_length)

        return max_length






"""
给定一个整数数组和一个整数 k，你需要在数组里找到 不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。
这里将 k-diff 数对定义为一个整数对 (nums[i], nums[j])，并满足下述全部条件：
0 <= i < j < nums.length
|nums[i] - nums[j]| == k

注意，|val| 表示 val 的绝对值。 

示例 1：
输入：nums = [3, 1, 4, 1, 5], k = 2
输出：2
解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个1，但我们只应返回不同的数对的数量。

示例 2：
输入：nums = [1, 2, 3, 4, 5], k = 1
输出：4
解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。

示例 3：
输入：nums = [1, 3, 1, 5, 4], k = 0
输出：1
解释：数组中只有一个 0-diff 数对，(1, 1)。

提示：
1 <= nums.length <= 10^4
-10^7 <= nums[i] <= 10^7
0 <= k <= 10^7

"""


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:


        # 方法一：哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        from collections import defaultdict
        count = defaultdict(int)
        for i, num in enumerate(nums):
            count[num] += 1

        ans = 0
        for num, time in count.items():
            if num + k in count:
                if (k == 0 and time > 1) or k > 0:
                    ans += 1
        return ans


        # 方法二：排序 + 双指针
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        nums.sort()
        n = len(nums)
        i, j = 0, 0

        ans = 0
        while i < n and j < n:
            #print(i, j)
            while j < n and nums[j] - nums[i] < k:
                j += 1
            while j + 1 < n and nums[j + 1] == nums[j]:
                j += 1
            #print('1:', i, j)
            if j < n and i != j and nums[j] - nums[i] == k:
                ans += 1
            while i + 1 < n and nums[i + 1] == nums[i]:
                i += 1
            i += 1
            #print('2:', i, j)
        
        return ans
        


"""
给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现 两次 的整数，并以数组形式返回。
你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。

示例 1：
输入：nums = [4,3,2,7,8,2,3,1]
输出：[2,3]

示例 2：
输入：nums = [1,1,2]
输出：[1]

示例 3：
输入：nums = [1]
输出：[]

提示：
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
nums 中的每个元素出现 一次 或 两次

"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:


        # 方法一：位运算
        # 时间复杂度：O(n)
        # 空间复杂度：O(logn)
        n = len(nums)

        res = []
        count = 0
        for i, num in enumerate(nums):
            if count & (1 << num) != 0:
                res.append(num)
            count |= (1 << num)

        return res


        # 方法二：原地哈希
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        i = 0

        res = set()
        while i < n:
            #print('i:', i)
            #print(nums)
            #print(nums[i], nums[nums[i] - 1])
            if nums[i] == nums[nums[i] - 1]:
                if (i + 1) != nums[i]: 
                    res.add(nums[i])
                i += 1
            else:
                tmp1 = nums[nums[i] - 1]
                tmp2 = nums[i]
                nums[nums[i] - 1] = tmp2
                nums[i] = tmp1
                

        return list(res)


        # 方法三：原地哈希
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                #print(nums)
            #print(i, nums)
        #print(nums)
        return [num for i, num in enumerate(nums) if num - 1 != i]


        # 方法四：使用正负号
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        ans = []
        for x in nums:
            x = abs(x)
            if nums[x - 1] > 0:
                nums[x - 1] = -nums[x - 1]
            else:
                ans.append(x)
        #print(nums)
        return ans




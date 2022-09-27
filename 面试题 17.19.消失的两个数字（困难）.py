"""
给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？
以任意顺序返回这两个数字均可。

示例 1:
输入: [1]
输出: [2,3]

示例 2:
输入: [2,3]
输出: [1,4]

提示：
nums.length <= 30000

"""

class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:


        # 方法一：位运算
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums) + 2

        count = 0
        for num in nums:
            count |= (1 << (num - 1))

        ans = []
        for i in range(1, n + 1):
            if (count >> (i - 1)) & 1 != 1:
                ans.append(i)
        return ans


        # 方法二：位运算
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        xorsum = 0
        n = len(nums) + 2
        for num in nums:
            xorsum ^= num
        for i in range(1, n + 1):
            xorsum ^= i
        
        lsb = xorsum & (-xorsum)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num
        for i in range(1, n + 1):
            if i & lsb:
                type1 ^= i
            else:
                type2 ^= i
        
        return [type1, type2]




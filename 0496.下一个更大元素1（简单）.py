"""
给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:


        # 方法一：暴力法
        # 时间复杂度：O(m * n)
        # 空间复杂度:O(m)
        m, n = len(nums1), len(nums2)
        if n == 1:
            return [-1]

        res = []
        for num in nums1:
            i = nums2.index(num)
            j = i + 1
            while j < n and num > nums2[j]:
                j += 1

            if j == n:
                res.append(-1)
            else:
                res.append(nums2[j])

        return res


        # 方法二：单调栈 + 哈希表
        # 时间复杂度：O(m + n)
        # 空间复杂度:O(m)
        res = {}
        stack = []

        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop(-1)
            res[num] = stack[-1] if stack else -1
            stack.append(num)

        return [res[num] for num in nums1]




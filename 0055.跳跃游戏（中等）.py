"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if 0 not in nums:
            return True

        # 方法一：数组
        # 时间复杂度：O(nm) ,其中n为nums长度，m为nums最大值
        # 空间复杂度：O(n)

        n = len(nums)
        res = [False] * (n)
        res[0] = True

        for i in range(n):
            if res[i] == True:
                num = nums[i]
                for j in range(1, num+1):
                    if i+j < n:
                        res[i+j] = True

        #print(res)
        return res[n-1]


        # 方法二：贪心
        # 时间复杂度：O(n) ,其中n为nums长度
        # 空间复杂度：O(1)
        n = len(nums)
        max_num = 0

        for i in range(n):
            if i > max_num:
                return False
            max_num = max(max_num, i + nums[i])

        return max_num >= n-1


        # 方法三：贪心2
        # 时间复杂度：O(n) ,其中n为nums长度
        # 空间复杂度：O(1)
        n = len(nums)
        max_num = 0

        for i in range(n):
            if i <= max_num:
                max_num = max(max_num, i + nums[i])
            if max_num >= n-1:
                return True

        return False


"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        # 方法一：回溯
        # 时间复杂度：O(n * n!)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 1:
            return [nums]

        ans = []
        res = []
        def backtrace(index, res):
            #print('index:', index)
            #print('res:', res)
            if index == n:
                ans.append(res[::1])
                return 
            for i in range(0, n):
                if nums[i] not in res:
                    res.append(nums[i])
                    backtrace(index + 1, res)
                    res.pop(-1)

        backtrace(0, res)
        return ans


        # 方法二：回溯2
        # 时间复杂度：O(n * n!)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 1:
            return [nums]

        ans = []
        def backtrace(index):
            #print('index:', index)
            #print('nums:', nums)
            if index == n:
                ans.append(nums[:])
                return 

            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index]
                backtrace(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        backtrace(0)
        return ans
            


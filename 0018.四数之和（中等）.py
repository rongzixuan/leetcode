"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
 
提示：
1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:


        # 方法一：排序 + 双指针
        # 时间复杂度：O(nlogn + n^2)
        # 空间复杂度：O(1)
        n = len(nums)
        if not nums or n < 4:
            return []
        nums.sort()
        #print('nums:', nums)

        res = []
        for a in range(n - 3):
            #print('a:', a)
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, n - 2):
                #print('b:', b)
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c, d = b + 1, n - 1
                #print(a, b, c, d)
                while c < d:
                    #print(a, b, c, d)
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        #print('true:', a, b, c, d)
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        d -= 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] < target:
                        c += 1
                    else:
                        d -= 1

        return res


        # 方法二：排序 + 双指针2
        # 时间复杂度：O(nlogn + n^2)
        # 空间复杂度：O(1)
        n = len(nums)
        if not nums or n < 4:
            return []
        nums.sort()
        #print('nums:', nums)

        res = []
        for a in range(n - 3):
            #print('a:', a)
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break
            if nums[a] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            for b in range(a + 1, n - 2):
                #print('b:', b)
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                if nums[a] + nums[b] + nums[b + 1] + nums[b + 2] > target:
                    break
                if nums[a] + nums[b] + nums[n - 2] + nums[n - 1] < target:
                    continue
                c, d = b + 1, n - 1
                #print(a, b, c, d)
                while c < d:
                    #print(a, b, c, d)
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        #print('true:', a, b, c, d)
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        d -= 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] < target:
                        c += 1
                    else:
                        d -= 1

        return res

             

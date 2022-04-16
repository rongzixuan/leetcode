"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]
 

提示：
0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        # 方法一：排序 + 双指针
        # 时间复杂度：O(nlogn + n^2)
        # 空间复杂度：O(1)
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        
        if nums[0] > 0 \
        or nums[-1] < 0 \
        or (nums[0] == 0 and nums[-1] > 0) \
        or (nums[0] < 0 and nums[-1] == 0):
            return []

        res = set()
        third = n - 1
        for first in range(n-2):
            for second in range(first + 1, n-1):
                #print('before:', first, second, third)
                if second >= third or first >= second:
                    break
                while third > second + 1 and nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                while third < n - 1 and nums[first] + nums[second] + nums[third] < 0:
                    third += 1
                if nums[first] + nums[second] + nums[third] == 0:
                    if (nums[first], nums[second], nums[third]) not in res:
                        res.add((nums[first], nums[second], nums[third]))
                    while third > second + 1 and nums[third - 1] == nums[third]:
                        third -= 1
                #print('after:', first, second, third)

        ans = list(res)
        return ans


        # 方法二：排序 + 双指针2
        # 时间复杂度：O(nlogn + n^2)
        # 空间复杂度：O(1)
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        
        if nums[0] > 0 \
        or nums[-1] < 0 \
        or (nums[0] == 0 and nums[-1] > 0) \
        or (nums[0] < 0 and nums[-1] == 0):
            return []

        res = set()
        third = n - 1
        for first in range(n-2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, n-1):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                #print('before:', first, second, third)
                if second >= third or first >= second:
                    break
                while third > second + 1 and nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                while third < n - 1 and nums[first] + nums[second] + nums[third] < 0:
                    third += 1
                if nums[first] + nums[second] + nums[third] == 0:
                    if (nums[first], nums[second], nums[third]) not in res:
                        res.add((nums[first], nums[second], nums[third]))
                    while third > second + 1 and nums[third - 1] == nums[third]:
                        third -= 1
                #print('after:', first, second, third)

        ans = list(res)
        return ans


        # 方法三：排序 + 双指针3
        # 时间复杂度：O(nlogn + n^2)
        # 空间复杂度：O(1)
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        
        if nums[0] > 0 \
        or nums[-1] < 0 \
        or (nums[0] == 0 and nums[-1] > 0) \
        or (nums[0] < 0 and nums[-1] == 0):
            return []

        res = []
        third = n - 1
        for first in range(n-2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, n-1):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                #print('before:', first, second, third)
                if second >= third or first >= second:
                    break
                while third > second + 1 and nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                while third < n - 1 and nums[first] + nums[second] + nums[third] < 0:
                    third += 1
                if nums[first] + nums[second] + nums[third] == 0:
                    res.append((nums[first], nums[second], nums[third]))
                    while third > second + 1 and nums[third - 1] == nums[third]:
                        third -= 1
                #print('after:', first, second, third)

        return res
                 







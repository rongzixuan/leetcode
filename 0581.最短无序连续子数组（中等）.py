"""
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
请你找出符合题意的 最短 子数组，并输出它的长度。

"""

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0 or n == 1:
            return 0

        # 方法一：遍历(双指针)
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        left, right = 0, n-1
        left_flag = False
        #right_flag = False

        i = 1
        while i < n:
            if nums[i] <= nums[i-1]:
                #print(i)
                if not left_flag and nums[i] < nums[i - 1]:
                    left = i - 1
                    left_flag = True
                    right = i
                    #right_flag = True
                    left_i = i
                    while left_i > 0 and nums[left_i] <= nums[left_i - 1]:
                        #print(i)
                        left = left_i - 1
                        left_i -= 1
                    while i < n and nums[i] <= nums[i-1]:
                        #print(i)
                        right = i
                        i += 1
                elif left_flag and nums[i] < nums[i-1]:
                    while i < n and nums[i] <= nums[i-1]:
                        #print(i)
                        right = i
                        i += 1
            i += 1

        return right - left + 1 if left_flag else 0


        # 方法二：遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
            
            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]
        
        #print(left, right)
        #print(minn, maxn)
        return 0 if right == -1 else right - left + 1


        # 方法三：排序
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        nums_copy = sorted(nums)
        #print(nums_copy)

        def judge_equal(nums, nums_copy):
            for i in range(n):
                if nums[i] != nums_copy[i]:
                    return False
            return True

        if judge_equal(nums, nums_copy) == True:
            return 0

        left, right = -1, n
        i = 0
        while nums_copy[i] == nums[i]:
            i += 1
        left = i

        j = n - 1
        while nums_copy[j] == nums[j]:
            j -= 1
        right = j

        print(left, right)
        return right - left + 1





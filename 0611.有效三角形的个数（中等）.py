"""
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。\

"""

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        # 方法一：排序 + 二分法
        # 时间复杂度：O(n*n*logn)
        # 空间复杂度：O(logn)
        nums.sort()
        n = len(nums)
        if n == 0:
            return 0
        res = 0

        for i in range(n-2):
            for j in range(i+1, n-1):
                sum2 = nums[i] + nums[j] # 两数之和
                # 二分法
                left, right = j+1, n-1
                while left <= right:
                    mid = left + (right-left) // 2
                    if nums[mid] >= sum2:
                        right = mid - 1
                    elif nums[mid] < sum2:
                        left = mid + 1
                #print('i, j, left, right:', i, j, left, right)
                count = right - j if right < n else 0
                res += count

        return res


        # 方法二：排序 + 双指针
        # 时间复杂度：O(n*n)
        # 空间复杂度：O(logn)
        nums.sort()
        n = len(nums)
        if n == 0:
            return 0

        res = 0

        for i in range(n-2):
            k = i
            for j in range(i+1, n-1):
                sum2 = nums[i] + nums[j]
                while k < n and nums[k] < sum2:
                    k += 1
                #print('i, j, k:', i, j, k)
                count = k - 1 - j if k-1 > j else 0
                res += count

        return res


        

                

"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

"""

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 方法一：双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 1 or nums[0] >= 0:
            return [num * num for num in nums]
        elif nums[-1] <= 0:
            return [num * num for num in nums][::-1]

        res = []
        i, j = 0, n-1
        # 找到绝对值最小的数
        while i < j:
            if abs(nums[i]) <= abs(nums[j]):
                j -= 1
            else:
                i += 1
        #print(i, j)

        while i >= -1 and j <= n-1 or i >= 0 and j <= n:
            #print(i, j)
            if i == j:
                i -= 1

            if i == -1:
                res.append(nums[j] * nums[j])
                j += 1
            elif j == n:
                res.append(nums[i] * nums[i])
                i -= 1
            else:    
                if abs(nums[i]) <= abs(nums[j]):
                    res.append(nums[i] * nums[i])
                    i -= 1
                else:
                    res.append(nums[j] * nums[j])
                    j += 1

        return res



        # 方法二：双指针2
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 1 or nums[0] >= 0:
            return [num * num for num in nums]
        elif nums[-1] <= 0:
            return [num * num for num in nums][::-1]

        i = j = 0
        negative = 0
        for i in range(n):
            if nums[i] < 0:
                negative = i

        i, j = negative, negative + 1
        print(i, j)

        res = []
        while i >= -1 and j <= n-1 or i >= 0 and j <= n:
            #print(i, j)
            if i == j:
                i -= 1

            if i == -1:
                res.append(nums[j] * nums[j])
                j += 1
            elif j == n:
                res.append(nums[i] * nums[i])
                i -= 1
            else:    
                if abs(nums[i]) <= abs(nums[j]):
                    res.append(nums[i] * nums[i])
                    i -= 1
                else:
                    res.append(nums[j] * nums[j])
                    j += 1

        return res


        # 方法三：双指针3
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 1 or nums[0] >= 0:
            return [num * num for num in nums]
        elif nums[-1] <= 0:
            return [num * num for num in nums][::-1]

        i, j = 0, n-1
        k = n-1
        res = [0] * n

        while k >= 0:
            if abs(nums[i]) <= abs(nums[j]):
                res[k] = nums[j] * nums[j]
                j -= 1
            else:
                res[k] = nums[i] * nums[i]
                i += 1
            k -= 1

        return res




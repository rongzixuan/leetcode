"""
如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。

"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:


        # 方法一：差分 + 计数
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        if n < 2:
            return 0

        sub_nums = []
        count = 0

        for i in range(1, n):
            sub_nums.append(nums[i] - nums[i-1])
        #print(sub_nums)

        index = 1
        while index < n - 1:
            #print(index)
            tmp_count = 0
            while index < n - 1 and sub_nums[index] == sub_nums[index - 1]:
                tmp_count += 1
                index += 1
            #print('index, tmp_count:', index, tmp_count)
            if tmp_count != 0:
                count += (1 + tmp_count) * tmp_count // 2
            index += 1

        return count



        # 方法二：差分 + 计数
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n < 3:
            return 0

        diff = nums[1] - nums[0]
        tmp_count = 0
        count = 0

        for i in range(2, n):
            if nums[i] - nums[i-1] == diff:
                tmp_count += 1
            else:
                diff = nums[i] - nums[i-1]
                tmp_count = 0
            count += tmp_count

        return count



        # 方法三：差分 + 计数
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n < 3:
            return 0

        diff = nums[1] - nums[0]
        tmp_count = 0
        count = 0
        i = 2

        while i < n:
            if (nums[i] - nums[i-1]) != diff:
                diff = nums[i] - nums[i-1]
                tmp_count = 0
                i += 1
            else:
                while i < n and (nums[i] - nums[i-1]) == diff:
                    tmp_count += 1
                    i += 1
                count += (1 + tmp_count) * tmp_count // 2

        return count






"""
元素的 频数 是该元素在一个数组中出现的次数。

给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。

执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。

"""

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        n = len(nums)

        # 方法一：排序+找差值(超时)
        nums.sort()
        #print(nums)
        
        sub = []       
        for i in range(1, n):
            sub.append(nums[i] - nums[i-1])
        #print(sub)

        max_frequence = 1
        for i in range(n-2, -1, -1):
            #print('i:', i)
            tmp_k = 0
            j = 1
            count = 1
            while j <= i+1:
                for index in range(j):
                    #if i == 11: 
                    #print('i-index:', i-index)
                    tmp_k += sub[i-index]                   
                if tmp_k <= k:
                    count += 1
                    max_frequence = max(max_frequence, count)
                    #if i == 11:
                    #print('max_frequence:', max_frequence)
                j += 1

        #print(max_frequence)
        return max_frequence


        # 方法二：排序 + 前缀和 + 二分 + 滑动窗口
        nums.sort()

        # 前缀和
        pre_sums = [0]
        pre_sum = 0
        for num in nums:
            pre_sum += num
            pre_sums.append(pre_sum)
        #print(pre_sums)

        # 滑动窗口
        def check(length, nums, pre_sums, k):
            #print('length:', length)
            n = len(nums)
            for i in range(n-1, length-2, -1):
                #print('i, i-length:', i, i-length)
                mid_sum = pre_sums[i+1] - pre_sums[i-length+1]
                #print('mid_sum:', mid_sum)
                if (length * nums[i] - mid_sum) <= k:
                    #print('True')
                    return True
            #print('False')
            return False

        # 二分查找
        left, right = 1, n
        while left < right:
            #print("left, right:", left, right)
            mid = (left + right + 1) >> 1
            if check(mid, nums, pre_sums, k) == True:
                left = mid
            elif check(mid, nums, pre_sums, k) == False:
                right = mid - 1
        return right 





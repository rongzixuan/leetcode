"""
统计一个数字在排序数组中出现的次数。

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        if n == 0:
            return 0

        # 方法一：二分法
        left, right = 0, n-1
        while left <= right:
            #print(left, right)
            mid = left + (right-left) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = right = mid
                while left-1 > -1:
                    if nums[left-1] == target:
                        left -= 1
                    else:
                        break
                while right+1 < n:
                    if nums[right+1] == target:
                        right += 1
                    else:
                        break
                return right - left + 1
            
        #print(left, right)
        return 0


        # 方法二：二分法
        def binarySearch(nums, target, firstFlag):
            n = len(nums)
            left, right = 0, n-1
            res = n
            while left <= right:
                #print(left, right)
                mid = left + (right-left) // 2
                if nums[mid] > target or (nums[mid] >= target and firstFlag):
                    right = mid - 1
                    res = mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    left = mid + 1
                else:
                    left = mid + 1
            return res
                
        first_index = binarySearch(nums, target, True)
        last_index = binarySearch(nums, target, False) - 1
        print(first_index, last_index)

        if first_index >= 0 \
        and last_index < n \
        and first_index <= last_index \
        and nums[first_index] == target \
        and nums[last_index] == target:
            return last_index - first_index + 1
        return 0


        # 方法三：二分法
  
        # 寻找左边界
        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:               
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        first_index = right + 1

        # 寻找右边界
        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:               
                right = mid - 1
            elif nums[mid] <= target:
                left = mid + 1
        last_index = right + 1

        return last_index - first_index


        # 方法四：二分法
        # 寻找右边界
        def binarySearch(nums, target):
            n = len(nums)
            left, right = 0, n-1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:               
                    right = mid - 1
                elif nums[mid] <= target:
                    left = mid + 1
            return left

        first_index = binarySearch(nums, target-1)
        last_index = binarySearch(nums, target)
        return last_index - first_index


    
    

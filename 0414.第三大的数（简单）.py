"""
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:


        # 方法一：排序
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        n = len(nums)
        if n < 3:
            return max(nums)

        nums.sort(reverse=True)
        print(nums)
        
        diff = 0
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                diff += 1
            if diff == 2:
                return nums[i]

        return nums[0]


        # 方法二：有序集合
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n < 3:
            return max(nums)

        from sortedcontainers import SortedList
        sl = SortedList()
        #print(sl)

        for i in range(n):
            if nums[i] not in sl:
                sl.add(nums[i])
            if len(sl) > 3:
                sl.pop(0)

        return sl[0] if len(sl) == 3 else sl[-1]


        # 方法三：一次遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n < 3:
            return max(nums)

        a, b, c = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > a:
                a, b, c = num, a, b
            elif a > num > b:
                b, c = num, b
            elif b > num > c:
                c = num

        return a if c == float('-inf') else c


        # 方法四：一次遍历2
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n < 3:
            return max(nums)

        a, b, c = None, None, None
        for num in nums:
            #print(num)
            if a == None or num > a:
                a, b, c = num, a, b
            elif a > num and (b is None or num > b):
                b, c = num, b
            elif b != None and b > num and (c is None or num > c):
                c = num

        return a if c == None else c




"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

 

进阶：

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？

"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # 方法一：使用额外数组
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        if n == 1:
            return nums

        res = [0] * n
        for i in range(n):
            #print(i, (i + k) % n)
            res[i] = nums[(i - k) % n]

        #print('nums:', nums)
        #print('res:', res)
        for i in range(n):
            nums[i] = res[i]
            

        # 方法二：双指针1
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 1 or k == n or k == 0:
            return nums

        import math
        count = math.gcd(n, k)
        #print('count:', count)
        #print('n // count:', n // count)

        for i in range(count):
            tmp = k % n + i
            #print('tmp:', tmp)
            pre, aft = nums[i], nums[i]       
            for i in range(n // count):
                #print('tmp:', tmp)
                #print('pre, aft:', pre, aft)
                pre = aft
                aft = nums[tmp]
                #print('tmp, (tmp - k) % n:', tmp, (tmp - k) % n)
                nums[tmp] = pre
                tmp = (tmp + k) % n
                #print('nums:', nums)

        return nums



        # 方法三：翻转数组
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 1 or k == n or k == 0:
            return nums

        def reverse(left, right):
            nums[left: right] = nums[left: right][::-1]

        reverse(0, n)
        reverse(0, k % n)
        reverse(k % n, n)











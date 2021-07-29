"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        # 方法一：双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)

        left, right = 0, n-1

        # 将0放在列表最前
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1

        # 将2放在列表最后
        for i in range(n-1, left-1, -1):
            if nums[i] == 2:
                #print(i)
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1

        return nums
        
        
        # 方法二：双指针（一次遍历）
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)

        left, right = 0, n-1
        i = 0

        while i <= right:
            #print('i, num[i]:', i, nums[i])
            while nums[i] == 2 and i <= right:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            #else:
                
            i += 1
            #print('nums:', nums)

        return nums



        # 方法三：双指针（一次遍历）
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)

        flag1 = flag0 = 0

        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[flag1] = nums[flag1], nums[i]
                flag1 += 1
            elif nums[i] == 0:
                nums[i], nums[flag0] = nums[flag0], nums[i]
                if flag0 < flag1:
                    nums[i], nums[flag1] = nums[flag1], nums[i]
                flag1 += 1
                flag0 += 1
        return nums



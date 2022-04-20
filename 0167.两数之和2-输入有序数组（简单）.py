"""
给定一个已按照 非递减顺序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        # 方法一：双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(numbers)
        if n == 2:
            return [1, 2]

        i, j = 0, n - 1
        while i < j:
            #print(i, j)
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1


        # 方法二：二分法
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        n = len(numbers)
        if n == 2:
            return [1, 2]

        for i in range(n):
            left, right = i+1, n-1
            while left <= right:
                #print(left, right)
                mid = left + ((right - left) >> 1)
                if numbers[i] + numbers[mid] == target:
                    return [i+1, mid+1]
                elif numbers[i] + numbers[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        





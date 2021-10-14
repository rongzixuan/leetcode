"""
符合下列属性的数组 arr 称为 山峰数组（山脉数组） ：

arr.length >= 3
存在 i（0 < i < arr.length - 1）使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i ，即山峰顶部。

"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        # 方法一：二分法
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        n = len(arr)
        if arr[0] > arr[1]:
            return 0
        elif arr[n-1] > arr[n-2]:
            return n-1

        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                left = mid + 1
            elif arr[mid] < arr[mid-1]:
                right = mid - 1

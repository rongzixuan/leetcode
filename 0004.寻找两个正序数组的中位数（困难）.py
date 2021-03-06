"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        # 方法一：二分法
        # 时间复杂度：O(log(m+n))
        # 空间复杂度：O(1)
        m, n = len(nums1), len(nums2)
        length = m + n

        def getKElement(k):
            i = j = 0

            while True:
                print('i, j, k:', i, j, k)
                if i == m:
                    return nums2[j + k - 1]
                elif j == n:
                    return nums1[i + k - 1]
                elif k == 1:
                    print(nums1[i], nums2[j])
                    return min(nums1[i], nums2[j])

                new_i = min(i + k // 2 - 1, m - 1)
                new_j = min(j + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[new_i], nums2[new_j]

                if pivot1 <= pivot2:
                    k -= (new_i - i + 1)
                    i = new_i + 1
                else:
                    k -= (new_j - j + 1)
                    j = new_j + 1 


        if length % 2 == 1:
            return getKElement((length + 1) // 2)
        else:
            return (getKElement(length // 2) + getKElement((length + 2) // 2)) / 2
        
        
        

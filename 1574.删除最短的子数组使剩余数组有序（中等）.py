"""
给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。

一个子数组指的是原数组中连续的一个子序列。

请你返回满足题目要求的最短子数组的长度。

示例 1：
输入：arr = [1,2,3,10,4,2,3,5]
输出：3
解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
另一个正确的解为删除子数组 [3,10,4] 。

示例 2：
输入：arr = [5,4,3,2,1]
输出：4
解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。

示例 3：
输入：arr = [1,2,3]
输出：0
解释：数组已经是非递减的了，我们不需要删除任何元素。

示例 4：
输入：arr = [1]
输出：0

提示：
1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9

"""


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:


        # 方法一：双指针 + 二分法
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        from bisect import bisect_left, bisect_right
        n = len(arr)
        i = 0
        while i + 1 < n and arr[i + 1] >= arr[i]:
            i += 1
        j = n - 1
        while j - 1 >= 0 and arr[j - 1] <= arr[j]:
            j -= 1
        #print('i, j:', i, j)

        if i >= j:
            return 0
        if arr[i] <= arr[j]:
            return j - i - 1

        ans = inf
        for i_ in range(0, i + 1):
            j_ = bisect_left(arr[j:], arr[i_])
            #print('i_, j_ + j:', i_, j_ + j)
            ans = min(ans, j + j_ - i_ - 1)
        for j_ in range(j, n):
            i_ = bisect_right(arr[:i + 1], arr[j_])
            #print('i_, j_:', i_, j_)
            ans = min(ans, j_ - i_)
        return ans


        # 方法二：双指针 + 二分法
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        n = len(arr)
        i, j = 0, n - 1
        while i + 1 < n and arr[i] <= arr[i + 1]:
            i += 1
        while j - 1 >= 0 and arr[j - 1] <= arr[j]:
            j -= 1
        if i >= j:
            return 0
        ans = min(n - i - 1, j)
        for l in range(i + 1):
            r = bisect_left(arr, arr[l], lo=j)
            ans = min(ans, r - l - 1)
        return ans


        # 方法三：双指针 + 二分法
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(arr)
        i, j = 0, n - 1
        while i + 1 < n and arr[i] <= arr[i + 1]:
            i += 1
        while j - 1 >= 0 and arr[j - 1] <= arr[j]:
            j -= 1
        if i >= j:
            return 0
        ans = min(n - i - 1, j)
        r = j
        for l in range(i + 1):
            while r < n and arr[r] < arr[l]:
                r += 1
            ans = min(ans, r - l - 1)
        return ans





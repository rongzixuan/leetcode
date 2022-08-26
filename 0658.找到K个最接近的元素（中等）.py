"""
给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：
|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b
 
示例 1：
输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]

示例 2：
输入：arr = [1,2,3,4,5], k = 4, x = -1
输出：[1,2,3,4]
 
提示：
1 <= k <= arr.length
1 <= arr.length <= 10^4
arr 按 升序 排列
-10^4 <= arr[i], x <= 10^4

"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:


        # 方法一：二分法 + 双指针
        # 时间复杂度：O(logn + k)
        # 空间复杂度：O(1)
        n = len(arr)
        from bisect import bisect_left
        index = bisect_left(arr, x)
        #print('index:', index)

        left, right = max(0, index - k), min(n - 1, index + k)
        #print(left, right)
        while right - left + 1 > k:
            #print(left, right)
            if arr[right] - x >= x - arr[left]:
                right -= 1
            else:
                left += 1

        return arr[left : right + 1]


        # 方法二：排序
        # 时间复杂度：O(nlogn + klogk)
        # 空间复杂度：O(1)
        arr.sort(key=lambda num: abs(num - x))
        return sorted(arr[:k])




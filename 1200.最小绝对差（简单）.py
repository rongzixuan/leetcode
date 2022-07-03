"""
给你个整数数组 arr，其中每个元素都 不相同。
请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

示例 1：
输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]

示例 2：
输入：arr = [1,3,6,10,15]
输出：[[1,3]]

示例 3：
输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]

提示：
2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6

"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:


        # 方法一：排序
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        arr.sort()
        ans = []
        min_sub = float('inf')
        for i, num in enumerate(arr):
            if i > 0 and arr[i] - arr[i - 1] < min_sub:
                min_sub = arr[i] - arr[i - 1]
                ans = []
                ans.append([arr[i - 1], arr[i]])
            elif i > 0 and arr[i] - arr[i - 1] == min_sub:
                ans.append([arr[i - 1], arr[i]])

        return ans
        
        
        

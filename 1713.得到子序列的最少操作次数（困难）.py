"""
给你一个数组 target ，包含若干 互不相同 的整数，以及另一个整数数组 arr ，arr 可能 包含重复元素。

每一次操作中，你可以在 arr 的任意位置插入任一整数。比方说，如果 arr = [1,4,1,2] ，那么你可以在中间添加 3 得到 [1,4,3,1,2] 。你可以在数组最开始或最后面添加整数。

请你返回 最少 操作次数，使得 target 成为 arr 的一个子序列。

一个数组的 子序列 指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。比方说，[2,7,4] 是 [4,2,3,7,2,1,4] 的子序列（加粗元素），但 [2,4,2] 不是子序列。

"""

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:

        # 方法一：贪心 + 二分法
        n, m = len(target), len(arr)

        # 建立哈希映射
        hash_table = {}
        for i in range(n):
            hash_table[target[i]] = i
        #print(hash_table)

        # 将arr映射
        arr_ = []
        for a in arr:
            if a in hash_table:
                arr_.append(hash_table[a])
        #print(arr_)

        # 二分法找arr_的最长严格上升子序列
        res = []

        for a in arr_:
            if len(res) == 0 or res[-1] < a:
                res.append(a)
            else:
                left, right = 0, len(res)
                while left <= right:
                    #print(left, right)
                    mid = left + (right - left) // 2
                    if res[mid] < a:
                        left = mid + 1
                    else:
                        right = mid - 1
                res[left] = a

        return n - len(res)





"""
给你一个大小为 m * n 的矩阵 mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。

请你返回矩阵中战斗力最弱的 k 行的索引，按从最弱到最强排序。

如果第 i 行的军人数量少于第 j 行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。

军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。

"""

class Helper:

    @staticmethod
    def partition(arr, left, right):
        pivot = arr[right]
        index = left - 1

        for i in range(left, right):
            if arr[i] <= pivot:
                index += 1
                arr[index], arr[i] = arr[i], arr[index]

        arr[right], arr[index+1] = arr[index+1], arr[right]
        return index + 1 

    @staticmethod
    def quickSort(arr, left, right, k):
        pivot = random.randint(left, right)
        arr[pivot], arr[right] = arr[right], arr[pivot]
        pos = Helper.partition(arr, left, right)
        count = pos - left + 1 

        if count < k:
            Helper.quickSort(arr, pos+1, right, k-count)
        elif count > k:
            Helper.quickSort(arr, left, pos-1, k)

    @staticmethod
    def getMinimizeK(arr, k):
        n = len(arr)
        Helper.quickSort(arr, 0, n-1, k)
        return arr[:k]


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:


        # 方法一：二分法 + 小根堆
        # 时间复杂度：O(mlogn + klogm)
        # 空间复杂度：O(m)
        m, n = len(mat), len(mat[0])
        count = []
        res = []

        for i in range(m):
            ma = mat[i]
            left, right = 0, n-1
            while left <= right:
                mid = left + (right - left) // 2
                if ma[mid] == 1:
                    left = mid + 1
                else:
                    right = mid - 1
            count.append((right+1, i))
        #print(count)

        # 转换成小根堆
        heapq.heapify(count)
        #print(count)

        for i in range(k):
            res.append(heapq.heappop(count)[1])
        return res


        # 方法二：二分法 + 快排思想
        # 时间复杂度：O(mlogn + klogk)
        # 空间复杂度：O(m)
        m, n = len(mat), len(mat[0])
        count = []
        res = []

        for i in range(m):
            left, right = 0, n-1
            while left <= right:
                mid = left + (right - left) // 2
                if mat[i][mid] == 1:
                    left = mid + 1
                else:
                    right = mid - 1
            count.append((right+1, i))

        #print(count)
        minimize = Helper.getMinimizeK(count, k)
        minimize.sort()

        #print(minimize)

        return [mi[1] for mi in minimize] 








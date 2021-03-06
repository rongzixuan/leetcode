"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

"""

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        if k == 0:
            return []

        # 方法一：排序
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        arr.sort()
        return arr[:k]


        # 方法二：大根堆
        # 时间复杂度：O(nlogk)
        # 空间复杂度：O(k)
        n = len(arr)
        a = [-x for x in arr[:k]] 
        heapq.heapify(a) # 用负数建立大根堆
        
        for i in range(k, n):
            if arr[i] < -a[0]:
                heapq.heappop(a)
                heapq.heappush(a, -arr[i])

        res = [-x for x in a]
        return res


        # 方法三：快排
        # 时间复杂度：O(n)
        # 空间复杂度：O(logn)

        def partition(arr, left, right):
            pivot = arr[right]
            index = left - 1
            for i in range(left, right):
                if arr[i] <= pivot:
                    index += 1
                    arr[i], arr[index] = arr[index], arr[i]

            arr[right], arr[index+1] = arr[index+1], arr[right]
            return index + 1

        def random_selected(arr, left, right, k):
            pivot = random.randint(left, right)
            arr[pivot], arr[right] = arr[right], arr[pivot]
            pos = partition(arr, left, right)
            count = pos - left + 1

            if count > k:
                random_selected(arr, left, pos - 1, k)
            elif count < k:
                random_selected(arr, pos + 1, right, k - count)


        n = len(arr)
        random_selected(arr, 0, n-1, k)
        return arr[:k]



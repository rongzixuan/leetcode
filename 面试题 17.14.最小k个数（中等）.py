"""
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

"""

class Solution:

    def smallestK(self, arr: List[int], k: int) -> List[int]:

        n = len(arr)
        if k == 0 or n == 0:
            return []

        # 方法一：排序
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(logn)
        arr.sort()
        return arr[:k]


        # 方法二：最大堆
        # 时间复杂度：O(nlogk)
        # 空间复杂度：O(k)
        heap = [-x for x in arr[:k]]
        heapq.heapify(heap)

        for i in range(k, n):
            if arr[i] < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -arr[i])

        return [-x for x in heap]



        # 方法三：快排思想
        # 时间复杂度：O(n)
        # 空间复杂度：O(logn)
        def randomChoose(arr, left, right):
            pivot = random.randint(left, right)
            #print('pivot:', pivot)
            #print('arr:', arr[left: right+1])
            arr[pivot], arr[right] = arr[right], arr[pivot]

            count = 0
            for i in range(left, right):
                if arr[i] < arr[right]:
                    count += 1
                    arr[i], arr[count+left-1] = arr[count+left-1], arr[i]
            
            arr[right], arr[count+left] = arr[count+left], arr[right]
            #print('arr:',arr)
            #print('count:', count)
            return count + 1


        def chooseK(arr, left, right, k):
            #print('left, right, k:', left, right, k)
            count = randomChoose(arr, left, right)

            #print('count + left:', count + left)
            if count + left < k:
                chooseK(arr, left + count, right, k)
            elif count + left > k:
                chooseK(arr, left, left + count - 1, k)
 

        chooseK(arr, 0, n-1, k)
        return arr[: k]



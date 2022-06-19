"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        # 方法一：优先队列（大根堆）
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(nums)
        if k == 1 or n == 1:
            return nums

        max_nums = []
        #heap = nums[0:k]
        heap = [(-nums[i], i) for i in range(k)]
        #print(heap)
        heapq.heapify(heap)
        #print(heap)
        max_nums.append(-heap[0][0])
        #print(max_nums)

        for i in range(k, n):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            max_nums.append(-heap[0][0])

        return max_nums



        # 方法二：遍历——超时
        # 时间复杂度：O(n*n)
        # 空间复杂度：O(k)
        n = len(nums)
        if k == 1 or n == 1:
            return nums

        max_nums = []
        last_max = (nums[0], 0)
        from collections import deque
        deq = deque()

        for i in range(0, k):
            deq.append(nums[i])
            if nums[i] > last_max[0]:
                last_max = (nums[i], i)
        max_nums.append(last_max[0])
        #print(deq)

        for i in range(k, n):
            deq.append(nums[i])
            deq.popleft()
            if nums[i] > last_max[0]:
                last_max = (nums[i], i)
                max_nums.append(nums[i])
            elif last_max[1] != i - k:
                max_nums.append(last_max[0])
            else:
                last_max = (nums[i-k+1], i-k+1)
                for j in range(i-k+2, i+1):
                    if nums[j] >= last_max[0]:
                        last_max = (nums[j], j)
                max_nums.append(last_max[0])

        return max_nums


        # 方法三：单调队列（双端队列）
        # 时间复杂度：O(n)
        # 空间复杂度：O(k)
        n = len(nums)
        if k == 1 or n == 1:
            return nums

        res = []
        from collections import deque
        deq = deque()

        for i in range(0, k):
            while deq and nums[i] >= deq[-1][0]:
                deq.pop()
            deq.append((nums[i], i))
        res.append(deq[0][0])

        for i in range(k, n):
            while deq and nums[i] >= deq[-1][0]:
                deq.pop()
            deq.append((nums[i], i))

            while deq[0][1] <= i - k:
                deq.popleft()

            res.append(deq[0][0])

        return res


    

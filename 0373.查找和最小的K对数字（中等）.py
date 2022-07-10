"""
给定两个以 升序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。
定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。
请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。

示例 1:
输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
     
示例 2:
输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
     
示例 3:
输入: nums1 = [1,2], nums2 = [3], k = 3 
输出: [1,3],[2,3]
解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]

提示:
1 <= nums1.length, nums2.length <= 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 和 nums2 均为升序排列
1 <= k <= 1000

"""


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:


        # 方法一：优先队列（堆）
        # 时间复杂度：O(klogk)
        # 空间复杂度：O(k)
        m, n = len(nums1), len(nums2)
        import heapq
        #heap = []
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        #heapq.heappush(heap, [nums1[0] + nums2[0], 0, 0])
        #print(heap)

        res = []
        while len(res) < k and heap:
            num, i, j = heapq.heappop(heap)
            #print('num, i, j:', num, i, j)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res


        m, n = len(nums1), len(nums2)

        # 二分查找第 k 小的数对和
        left, right = nums1[0] + nums2[0], nums1[m - 1] + nums2[n - 1] + 1
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            i, j = 0, n - 1
            while i < m and j >= 0:
                if nums1[i] + nums2[j] > mid:
                    j -= 1
                else:
                    cnt += j + 1
                    i += 1
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        pairSum = left

        ans = []
        # 找数对和小于 pairSum 的数对
        i = n - 1
        for num1 in nums1:
            while i >= 0 and num1 + nums2[i] >= pairSum:
                i -= 1
            for j in range(i + 1):
                ans.append([num1, nums2[j]])
                if len(ans) == k:
                    return ans

        # 找数对和等于 pairSum 的数对
        i = n - 1
        for num1 in nums1:
            while i >= 0 and num1 + nums2[i] > pairSum:
                i -= 1
            j = i
            while j >= 0 and num1 + nums2[j] == pairSum:
                ans.append([num1, nums2[j]])
                if len(ans) == k:
                    return ans
                j -= 1
        return ans


        # 方法二：二分法 + 双指针
        # 时间复杂度：O()
        # 空间复杂度：O(1)
        m, n = len(nums1), len(nums2)

        def getKNum(nums1, nums2):
            # 二分查找第k小的对数
            m, n = len(nums1), len(nums2)
            left, right = nums1[0] + nums2[0], nums1[-1] + nums2[-1]
            #pair = -1
            while left <= right:
                mid = left + (right - left) // 2
                i, j = 0, n - 1
                count = 0
                while i < m and j >= 0: 
                    #print(i, j)
                    if nums1[i] + nums2[j] <= mid:                       
                        count += j + 1
                        i += 1
                    elif nums1[i] + nums2[j] > mid: 
                        j -= 1
                #print(left, right, mid)
                #print('count:', count)
                if count > k:
                    right = mid - 1
                elif count < k:
                    left = mid + 1
                else:
                    print(mid)
                    return mid
            print(left)
            return left

        pair = getKNum(nums1, nums2)

        res = []
        # 找数对和小于 pairSum 的数对
        i = n - 1
        for num1 in nums1:
            while i >= 0 and num1 + nums2[i] >= pair:
                i -= 1
            for j in range(i + 1):
                res.append([num1, nums2[j]])
                if len(res) == k:
                    return res

        # 找数对和等于 pairSum 的数对
        i = n - 1
        for num1 in nums1:
            while i >= 0 and num1 + nums2[i] > pair:
                i -= 1
            j = i
            while j >= 0 and num1 + nums2[j] == pair:
                res.append([num1, nums2[j]])
                if len(res) == k:
                    return res
                j -= 1

        return res




"""
给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。
每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。
请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 -1 。

示例 1：
输入：nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
输出：3
解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
- 将 nums2[0] 变为 6 。 nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2] 。
- 将 nums1[5] 变为 1 。 nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2] 。
- 将 nums1[2] 变为 2 。 nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2] 。

示例 2：
输入：nums1 = [1,1,1,1,1,1,1], nums2 = [6]
输出：-1
解释：没有办法减少 nums1 的和或者增加 nums2 的和使二者相等。

示例 3：
输入：nums1 = [6,6], nums2 = [1]
输出：3
解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
- 将 nums1[0] 变为 2 。 nums1 = [2,6], nums2 = [1] 。
- 将 nums1[1] 变为 2 。 nums1 = [2,2], nums2 = [1] 。
- 将 nums2[0] 变为 4 。 nums1 = [2,2], nums2 = [4] 。

提示：
1 <= nums1.length, nums2.length <= 10^5
1 <= nums1[i], nums2[i] <= 6

"""

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:


        # 方法一：哈希表 + 贪心
        # 时间复杂度：O(n + m)
        # 空间复杂度：O(C)
        # C = 6
        n, m = len(nums1), len(nums2)
        n1, n2 = max(n, m), min(n, m)
        if n1 > 6 * n2:
            return -1

        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0
        elif sum1 < sum2:
            return self.minOperations(nums2, nums1)

        from collections import Counter
        count1, count2 = Counter(nums1), Counter(nums2)
        #print(count1, count2)
        ans = 0
        while sum1 > sum2:
            #tmp = sum1 - sum2
            for i in range(6, 1, -1):
                while sum1 > sum2 and count1[i] > 0:
                    tar = max(1, i - sum1 + sum2)
                    count1[i] -= 1
                    count1[tar] += 1
                    sum1 -= (i - tar)
                    #tmp -= (i - tar)                      
                    ans += 1
                while sum1 > sum2 and count2[7 - i] > 0:
                    tar = min(6, 7 - i + sum1 - sum2)
                    count2[7 - i] -= 1
                    count2[tar] += 1
                    sum2 += (tar + i - 7)
                    #tmp -= (tar + i - 7)                          
                    ans += 1
            #print(count1, count2, sum1, sum2, sum1 - sum2)
        return ans


        # 方法二：哈希表 + 贪心
        # 时间复杂度：O(n + m)
        # 空间复杂度：O(C)
        # C = 6
        if 6 * len(nums1) < len(nums2) or 6 * len(nums2) < len(nums1):
            return -1  # 优化
        d = sum(nums2) - sum(nums1)  # 数组元素和的差，我们要让这个差变为 0
        if d < 0:
            d = -d
            nums1, nums2 = nums2, nums1  # 统一让 nums1 的数变大，nums2 的数变小
        ans = 0
        # 统计每个数的最大变化量（nums1 的变成 6，nums2 的变成 1）
        cnt = Counter(6 - x for x in nums1) + Counter(x - 1 for x in nums2)
        for i in range(5, 0, -1):  # 从大到小枚举最大变化量 5 4 3 2 1
            if i * cnt[i] >= d:  # 可以让 d 变为 0
                return ans + (d + i - 1) // i
            ans += cnt[i]  # 需要所有最大变化量为 i 的数
            d -= i * cnt[i]







